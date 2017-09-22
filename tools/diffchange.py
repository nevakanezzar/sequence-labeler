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

    with open(source_filename, "w") as source_file:
        for record in sources:
            source_file.write(record + "\n")
    print("Wrote {}".format(source_filename))

    with open(target_filename, "w") as target_file:
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
	if "<" in p1 or ">" in p1:
		p2 = remove_text_between(p1,"<ref","</ref>")
		if "<" in p2 or ">" in p2: #remove any leftover tags
			p2 = remove(p2,"<",">")
	else:
		p2 = p1
	if "[" in p2 or ']' in p2:
		parsed_sent = remove(p2,"\[","\]",1)
	else:
		parsed_sent = p2
	return parsed_sent.lstrip()

#CONSTANTS
WIKI_URL = "https://en.wikipedia.org"
WIKI_RANDOM = 'https://en.wikipedia.org/wiki/Special:Random'
INC_FILE = "wiki_incorrect_parallel_corpus.txt"
COR_FILE = "wiki_corrected_parallel_corpus.txt"

#initialisations
incorrect = []
corrected = []

try:
	while(True):
		r = requests.get(WIKI_RANDOM)
		if r.status_code != requests.codes.ok:
			continue
		url_2 = r.url.split("/")
		url_3 = "https://en.wikipedia.org/w/index.php?title="+url_2[-1]+"&offset=&limit=500&action=history"

		r2 = requests.get(url_3)
		if r2.status_code != requests.codes.ok:
			continue

		text = html.unescape(r2.text)

		if 'grammar' in text.lower():
			grammar_indices = [m.start() for m in re.finditer("grammar", text.lower())]
			print(grammar_indices)
			for i in range(len(grammar_indices)):
				grammar_index = grammar_indices[i] #text.find("grammar")
				prev_index = text[:grammar_index].rfind('prev')
				href_index = text[:prev_index].rfind('href')
				# print(text[grammar_index:grammar_index+10])
				# print(text[prev_index-10:prev_index+10])
				# print(text[href_index:href_index+100])
				url_start_index = text[href_index:].find("\"")+href_index
				url_end_index = text[url_start_index+1:].find("\"")+url_start_index+1
				url2 = WIKI_URL+text[url_start_index+1:url_end_index]
				print(url2)
				r3 = requests.get(url2)
				r3soup = BeautifulSoup(r3.text,'lxml')

				deletions = r3soup.find_all("td",class_="diff-deletedline")
				additions = r3soup.find_all("td",class_="diff-addedline")

				try:
					assert len(deletions) == len(additions)
				except:
					print("Lengths not the same!", len(deletions),len(additions))
					continue

				for block in range(len(additions)):
					a = additions[block].get_text()
					d = deletions[block].get_text()

					
					a0 = parse_brac(a)
					d0 = parse_brac(d)
					a1 = custom_parser(a0)
					d1 = custom_parser(d0)

					i = 0
					for q,w in zip(a1,d1):
						i+=1
						if q!=w: break

					for sent_start1 in re.finditer(r"[a-zA-z0-9\"\'][\.\?!] ", a1[:i-1]):
						pass

					try:
						sent_start = sent_start1.start() + 2
						try:
							sent_end_a = re.search(r"\. [A-Z]", a1[i:]).start() + i+2
						except AttributeError:
							sent_end_a = len(a1)
						try:
							sent_end_d = re.search(r"\. [A-Z]", d1[i:]).start() + i+2
						except AttributeError:
							sent_end_d = len(d1)

						inc = d1[sent_start:sent_end_d].strip()
						cor = a1[sent_start:sent_end_a].strip()
						print("I:",inc,"\nC:",cor)
						if len(inc)>5:
							incorrect += [inc]
							corrected += [cor]
					except NameError:
						print(a)
						print(a0)
						print(d0)
						print(a1)
						print(d1)

						print(i)
						print(a1[i-10:i+10])
						print(d1[i-10:i+10])

						print("Something went wrong... skipping")
						continue



except KeyboardInterrupt:
	x = input("\nSave (y/n) :")
	if 'y' in x.lower():
		output_dir = './wiki'
		write_parallel_text(incorrect, corrected, output_dir)



