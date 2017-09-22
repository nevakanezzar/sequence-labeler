import sys
import os
import requests
from bs4 import BeautifulSoup
import time
import html
import re
import collections


def write_parallel_text(sources, targets, output_prefix):
	"""
	Writes two files where each line corresponds to one example
		- [output_prefix].sources.txt
		- [output_prefix].targets.txt

	Args:
		sources: Iterator of source strings
		targets: Iterator of target strings
		output_prefix: Prefix for the output file
	"""
	source_filename = os.path.abspath(os.path.join(output_prefix, "sources.txt"))
	target_filename = os.path.abspath(os.path.join(output_prefix, "targets.txt"))

	with open(source_filename, "a") as source_file:
		for record in sources:
			source_file.write(record + "\n")
	print("Wrote {}".format(source_filename))

	with open(target_filename, "a") as target_file:
		for record in targets:
			target_file.write(record + "\n")
	print("Wrote {}".format(target_filename))



def remove(s,left_brac,right_brac, length_offset = 0):
	parsed_sent = ''
	left_angles = [m.start() for m in re.finditer(left_brac,s)]
	right_angles = [m.start() for m in re.finditer(right_brac,s)]
	len_right = len(right_brac) - length_offset
	
	if len(left_angles) == 0:
		if len(right_angles) == 1:
			return s[right_angles[0]+len_right:]
		else:
			return "!FAIL!"
			#todo
			print("Error 51601: don't know what to do with mis-matched brackets!")
			print(left_brac,right_brac,left_angles, right_angles,s)
			raise()
	elif len(right_angles) == 0:
		if len(left_angles) == 1:
			return s[:left_angles[0]]
		else:
			return "!FAIL!"
			#todo
			print("Error 51602: don't know what to do with mis-matched brackets!")
			print(left_brac,right_brac,left_angles, right_angles,s)
			raise()
	
	elif left_angles[0] > right_angles[0]:
		right_angles = right_angles[1:]

	try:
		assert len(left_angles) == len(right_angles)
	except:
		print("Error 51603: Assertion failed len(left_angles) == len(right_angles)")
		print(s)
		print([m.start() for m in re.finditer(left_brac,s)])
		print([m.start() for m in re.finditer(right_brac,s)])
		return "!FAIL!"
	parsed_sent += s[0:left_angles[0]]
	for i in range(len(left_angles)-1):
		parsed_sent += s[right_angles[i]+len_right:left_angles[i+1]]
	parsed_sent += s[right_angles[-1]+len_right:]
	return parsed_sent


def remove_text_between(s,left_brac,right_brac):
	parsed_sent = ''
	left_len = len(left_brac)
	right_len = len(right_brac)
	left_angles = [m.start() for m in re.finditer(left_brac,s)]
	right_angles = [m.start()+right_len for m in re.finditer(right_brac,s)]

	try:
		assert len(left_angles) == len(right_angles)
	except:
		return s
		# print(left_angles, right_angles)
		if len(left_angles) == 1:
			return remove(s,"<",">")
		# input("Press ENTER...")
		if len(left_angles) > len(right_angles):
			offset = 0
			items_to_drop = []
			for ind, item in enumerate(left_angles[:-1]):
				if right_angles[ind+offset] > left_angles[ind+1]:
					items_to_drop += [left_angles[ind]]
					offset-=1
			for item in items_to_drop:
				left_angles.remove(item)
		# print(left_angles, right_angles)
		# input("Press ENTER...")
	
	parsed_sent += s[0:left_angles[0]]
	for i in range(len(left_angles)-1):
		parsed_sent += s[right_angles[i]:left_angles[i+1]]
	parsed_sent += s[right_angles[-1]:]
	return parsed_sent


def parse_brac(s):
	parsed_sent = ''
	# print(s)
	left_angles = [m.start() for m in re.finditer('\[\[',s)]
	right_angles = [m.start() for m in re.finditer('\]\]',s)]
	len_right = 2
	len_left = 2
	right_angles = [-len_right]+right_angles
	# print(right_angles, left_angles)
	if len(right_angles) == len(left_angles):
		s = s+"]]"
		right_angles = [m.start() for m in re.finditer('\]\]',s)]
		right_angles = [-len_right]+right_angles
	for i in range(len(left_angles)):
		parsed_sent += s[right_angles[i]+len_right:left_angles[i]]
		token = s[left_angles[i]+len_left:right_angles[i+1]]
		if "|" in token:
			token = token[token.rfind("|")+1:]
		parsed_sent += token
	parsed_sent += s[right_angles[-1]+len_right:]
	return parsed_sent


def custom_parser(s):
	p0 = s
	# print(p0)
	#remove citations
	if "{{" in s or "}}" in s:
		p1 = remove(p0,"{{","}}")
	else:
		p1 = p0
	# print(p1)
	#remove ref tags
	if "<ref" in p1 and "</ref>" in p1:
		p2 = remove_text_between(p1,"<ref","</ref>")
	else:
		p2 = p1
	if "<" in p2 or ">" in p2: #remove any leftover tags
		p2 = remove_text_between(p2,"<",">")
	if "[" in p2 or ']' in p2:
		parsed_sent = remove(p2,"\[","\]",1)
	else:
		parsed_sent = p2
		
	parsed_sent = parsed_sent.replace("&mdash;","-")
	parsed_sent = parsed_sent.replace("&ndash;","-")
	parsed_sent = parsed_sent.replace("&nbsp;"," ")
	parsed_sent = parsed_sent.replace("\"\"","\"")
	parsed_sent = parsed_sent.replace("'''","\"")
	parsed_sent = parsed_sent.replace("''","\"")
	parsed_sent = re.sub( '\s+', ' ', parsed_sent).strip()
	parsed_sent = re.sub( '\s\.', '.', parsed_sent).strip()

	return parsed_sent

#CONSTANTS
OUTPUT_DIR = './simplewiki/'
OUTPUT_FIL = OUTPUT_DIR + 'simplewikicorpus.txt'
WIKI_URL = "https://simple.wikipedia.org"
WIKI_RANDOM = 'https://simple.wikipedia.org/wiki/Special:Random'
WIKI_RANDOM_REVISIONS = 'https://simple.wikipedia.org/w/index.php?title=Special:Random&offset=&limit=500&action=history'
INC_FILE = "wiki_incorrect_parallel_corpus.txt"
COR_FILE = "wiki_corrected_parallel_corpus.txt"
DEBUG = False
debug_link = ['https://en.wikipedia.org/w/index.php?title=Anti-austerity_movement_in_Greece&diff=477586550&oldid=477507753']
INVALID_STRINGS = ["==",'===',"|","*","category:", "grammar","#"]

#initialisations
incorrect = []
corrected = []

def find_grammar_page():
	"""
	returns a random wikipedia edit history page with the word 'grammar' in it
	Args:
		None
	Outputs:
		requests object, text
	"""

	while True:
		r1 = requests.get(WIKI_RANDOM_REVISIONS)
		if r1.status_code != requests.codes.ok:
			print("Error 51605: get",r1.url,"failed, status code",r1.status_code)
		time.sleep(0.25)
		text = html.unescape(r1.text)
		if "grammar" in text.lower():
			return r1, text


def find_revision_pages(url_text):
	"""
	returns revision page links aligned to 'grammar' edits
	Args:
		url_text: requests.text object with webpage text
	Outputs:
		revision_links: list of webpages
	"""
	revision_links = []
	grammar_indices = [m.start() for m in re.finditer("grammar", url_text.lower())]
	# print("Grammar indices:",grammar_indices)

	for i in range(len(grammar_indices)):
		grammar_index = grammar_indices[i] 
		prev_index = url_text[:grammar_index].rfind('prev')
		href_index = url_text[:prev_index].rfind('href')
		url_start_index = url_text[href_index:].find("\"")+href_index
		url_end_index = url_text[url_start_index+1:].find("\"")+url_start_index+1
		url2 = WIKI_URL+url_text[url_start_index+1:url_end_index]
		revision_links+=[url2]

	return list(set(revision_links))

try:
	while(True):
		try:
			if DEBUG:
				links = debug_link
			else:
				r, text = find_grammar_page()
				links = find_revision_pages(text)

			# print("All links:",links)

			for link in links:
				
				# print(link)
				if "grammar" in link.lower():  
					continue 	#skip links with grammar in them, probably not what we are looking for
				
				r3 = requests.get(link)
				r3soup = BeautifulSoup(r3.text,'lxml')

				deletions = r3soup.find_all("td",class_="diff-deletedline")
				additions = r3soup.find_all("td",class_="diff-addedline")

				try:
					assert len(deletions) == len(additions)
				except:
					print("Error 51606: Lengths not the same!", len(deletions),len(additions), "skipping",link)
					continue

				for block in range(len(additions)):
					a = additions[block].get_text()
					d = deletions[block].get_text()
					if "==" in a:
						continue

					if DEBUG:
						print("1")
						print(a)
						print(d)
						input()
					
					a0 = parse_brac(a)
					d0 = parse_brac(d)
					if DEBUG:
						print("2")
						print(a0)
						print(d0)
						input()
				
					a1 = custom_parser(a0)
					d1 = custom_parser(d0)
					if DEBUG:
						print("3")
						print(a1)
						print(d1)
						input()

					i = 0
					for q,w in zip(a1,d1):
						i+=1
						if q!=w: break

					sent_start1 = None
					for sent_start1 in re.finditer(r"[a-zA-z0-9\"\'\)]{2}[\.\?!] ", a1[:i]):
						pass

					if DEBUG:
						print(sent_start1)
						input()

					try:
						if sent_start1 == None:
							sent_start = 0
						else:
							sent_start = sent_start1.start() + 3

						try:
							sent_end_a = re.search(r"\.(\"|) [A-Z](?<!(.\s[A-Z]| Dr| Ph| Mr|Mrs| Ms| Jr)\. [A-Z])", a1[sent_start:]).start() + sent_start+2
						except AttributeError:
							sent_end_a = len(a1)
						try:
							sent_end_d = re.search(r"\.(\"|) [A-Z](?<!(.\s[A-Z]| Dr| Ph| Mr|Mrs| Ms| Jr)\. [A-Z])", d1[sent_start:]).start() + sent_start+2
						except AttributeError:
							sent_end_d = len(d1)

						if DEBUG:
							print(i, a1[i:],sent_end_a)
							print(i, d1[i:],sent_end_d)
							input()


						inc = d1[sent_start:sent_end_d].strip()
						cor = a1[sent_start:sent_end_a].strip()
						
						skip = False
						if inc == "" or cor == "":
							skip = True
						if inc[:-1] in cor or cor[:-1] in inc:
							skip = True
						for string in INVALID_STRINGS:
							if (string.lower() in inc.lower()) or (string.lower() in cor.lower()):
								skip = True
								break
						if skip == True:
							continue
						
						if inc != cor:
							write_list = [link,d,a,inc,cor]
							# print(write_list)
							print("Incorrect:",inc,"\nCorrected:",cor)
							f = open(OUTPUT_FIL, 'a')
							for item in write_list:
								f.write("%s\n" % item)
							f.write("\n")
							f.close()
							incorrect += [inc]
							corrected += [cor]
					except NameError :
						print(a)
						print(a0)
						print(d0)
						print(a1)
						print(d1)

						print(i)
						print(a1[i-10:i+10])
						print(d1[i-10:i+10])

						print("Something went wrong... skipping")
						print("")
						continue
		except requests.exceptions.ConnectionError:
			print("Annoyed wikipedia... restarting after 10 seconds...")
			time.sleep(10)



except KeyboardInterrupt:
	x = input("Save (y/n) :")
	if 'y' in x.lower():
		output_dir = './wiki/'
		write_parallel_text(incorrect, corrected, output_dir)



