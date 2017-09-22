#!/bin/python3

import sys
import os
import time
import html
import re
import collections
import numpy as np
from nltk.tokenize import wordpunct_tokenize

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

	with open(source_filename, "w", encoding='utf-8') as source_file:
		for record in sources:
			record2 = " ".join(wordpunct_tokenize(record.strip()))+'\n'
			source_file.write(record2)
	print("Wrote {}".format(source_filename))

	with open(target_filename, "w", encoding='utf-8') as target_file:
		for record in targets:
			record2 = " ".join(wordpunct_tokenize(record.strip()))+'\n'
			target_file.write(record2)
	print("Wrote {}".format(target_filename))

#CONSTANTS
OUTPUT_DIR = './wiki/'
INPUT_FILES = [
				OUTPUT_DIR + 'datacorpus.txt',
				OUTPUT_DIR + 'datacorpus_1.txt',
				OUTPUT_DIR + 'datacorpus_3.txt',
				OUTPUT_DIR + 'datacorpus_2.txt'
				]

# INPUT_FIL = OUTPUT_DIR + 'datacorpus_1.txt'
INC_FILE = "wiki_incorrect_parallel_corpus.txt"
COR_FILE = "wiki_corrected_parallel_corpus.txt"
DEBUG = False
INVALID_STRINGS = ["! Common or alternate name", "File:",
					"!FAIL!",
					"==",
					'===',
					"|",
					"*",
					"category:",
					"grammar",
					"#",
					"\"\"",
					"''",
					"/>",
					"()",
					"http",
					"[[",
					'\x83','\x80','\xad','\x93','\x99','\x82','\xa0','\x84',
					'\x90','\\','\x85','\x81','\x9c','\x8e','\x9d','\x94',
					'\x91','\x98','\x8d','\x97','\x89','\x9f','\x96','\x8f',
					'`','\x88','\x95','\x8c','\x86','\x9a','\x92','\x9b','\x8b',
					'\x8a','\x9e','·','{','¸','®',']','¬','ø','á','','å','°',
					'à','í','~','ñ','¢','µ','×','«','ª','ò','?','Ö','é','î','±',
					'_','ó','Á','@','¨','Ø','&','Æ','=','»','¦','¾','´','ì','ä',
					'³','½','©','¯','É','$','æ','¿','Ó','¹','²','ü','ù','Â','§',
					'Å','Ä','º','!','â','þ','^','¥','Î','Ú','ã','ê','ð','<','¶',
					'ô','¤','>','}','¡','ú','Þ','ß','ç','ö','ë','+','¼','ý','ï',
					'è','£']
MIN_SENT_LEN = 4
MAX_SENT_LEN = 50

#initialisations
incorrect = []
corrected = []

inc_dict = collections.defaultdict(list)
cor_dict = collections.defaultdict(list)



if __name__ == '__main__':
	
	inc = []
	cor = []
	for INPUT_FIL in INPUT_FILES:
		total = failed = selected = 0
		with open(INPUT_FIL, 'r',encoding="latin-1") as f:
			i = f.readline().strip()
			while True:
				c = f.readline().strip()
				a3 = f.readline().strip()
				while a3 is not "":
					i = c
					c = a3
					a3 = f.readline().strip()

				total+=1
				# print(total, i,c)
				
				fail = False

				for string in INVALID_STRINGS:
					if string in i:
						fail = True
						break
					elif string in c:
						fail = True
						break

				i_len = len(i.split())
				c_len = len(c.split())
				if i_len < MIN_SENT_LEN:
					fail = True
				elif i_len > MAX_SENT_LEN:
					fail = True
				elif c_len < MIN_SENT_LEN:
					fail = True
				elif c_len > MAX_SENT_LEN:
					fail = True
				try:
					if not (i[0].isupper() or i[0].isdigit() or i[0]=='\"' or i[0]=='\''):  #starts with a start-like character
						fail = True

					if not (c[0].isupper() or c[0].isdigit() or c[0]=='\"' or c[0]=='\''):  #starts with a start-like character
						fail = True

					if not (i[-1] in '.?!\'\"'):  #ends with an end-like character
						fail = True

					if not (c[-1] in '.?!\'\"'):  #ends with an end-like character
						fail = True

				except:
					fail = True
				if (abs(c_len - i_len)>10):
					fail = True

				# if i[:-2] in c:
				# 	fail == True
				# elif c[:-2] in i:
				# 	fail == True

				if fail == False:
					inc += [i]
					cor += [c]
					inc_dict[i] = c  #keep only most recent copy
					cor_dict[c] = i  #keep only most recent copy
					selected += 1
				else:
					failed += 1
					# if np.random.random()>0.001:
					# 	print(i)
					# 	print(c,'\n')

				i = f.readline()
				if not i: break



		print("File:",INPUT_FIL,"Total:", total,"\tSelected:", selected,"Failed:",failed)


	print("\nTotal valid sentence pairs:",len(cor_dict.keys()))
	
	print("\nLooking for duplicates...")
	wrong_cors = set(inc_dict.keys()) & set(cor_dict.keys())
	print("Incorrect sentences which are also tagged as correct sentences:",len(wrong_cors))
	print("\nExamples:",list(wrong_cors)[:min(10,len(wrong_cors))])
	
	print("Removing these from the corpus...")
	for sent in wrong_cors:
		del cor_dict[sent]
	print("Total sentences remaining:",len(cor_dict.keys()))
	print('\n')

	cor = list(cor_dict.keys())
	inds = np.random.choice(len(cor),10)
	
	for ind in inds:
		print("Examples of final corpus:")
		print("Incorrect:",cor_dict[cor[ind]])
		print("Correct:  ",cor[ind])

	inc = []
	for sent in cor:
		inc += [cor_dict[sent]]

	print("\nSanity check, correct sentences:",len(cor),"\tincorrect sentences:",len(inc))
	try:
		assert len(cor) == len(inc)
	except:
		print("Sanity check FAILED!")
		raise AssertionError

	output_dir = './wiki/'
	write_parallel_text(inc, cor, output_dir)


# 	counter = 0
# 	while counter < len(inc):

# 	indices = [i for i, x in enumerate(my_list) if x == "whatever"]


# def f7(seq):
#     seen = set()
#     seen_add = seen.add
#     return [x for x in seq if not (x in seen or seen_add(x))]
