#!/bin/python3

import sys
import os
import time
import html
import re
import collections
import numpy as np

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

#CONSTANTS
OUTPUT_DIR = './wiki/'
INPUT_FILES = [OUTPUT_DIR + 'datacorpus.txt',
				OUTPUT_DIR + 'datacorpus_1.txt',
				OUTPUT_DIR + 'datacorpus_2.txt',
				OUTPUT_DIR + 'datacorpus_3.txt']

# INPUT_FIL = OUTPUT_DIR + 'datacorpus_1.txt'
INC_FILE = "wiki_incorrect_parallel_corpus.txt"
COR_FILE = "wiki_corrected_parallel_corpus.txt"
DEBUG = False
INVALID_STRINGS = ["! Common or alternate name", "!FAIL!","==",'===',"|","*","category:", "grammar","#","\"\"",
					"''","/>","()","http","[["]
MIN_SENT_LEN = 5
MAX_SENT_LEN = 50

#initialisations
incorrect = []
corrected = []


if __name__ == '__main__':
	
	inc = []
	cor = []
	for INPUT_FIL in INPUT_FILES:
		total = failed = selected = 0
		with open(INPUT_FIL, 'r',encoding="latin-1") as f:
			while True:
				_ = f.readline()
				_ = f.readline()
				_ = f.readline()
				i = f.readline().strip()
				c = f.readline().strip()
				total+=1
				
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

				if (abs(c_len - i_len)>10):
					fail = True

				# if i[:-2] in c:
				# 	fail == True
				# elif c[:-2] in i:
				# 	fail == True

				if fail == False:
					inc += [i]
					cor += [c]
					selected += 1
				else:
					failed += 1
				line = f.readline()
				if not line: break

		print("File:",INPUT_FIL,"Total:", total,"\tSelected:", selected,"Failed:",failed)
		# t = 1
		# for i,item in enumerate(inc):
		# 	j = 1
		# 	indices = []
		# 	num = 0
		# 	while (item in inc[j:]):
		# 		num += 1
		# 		j = inc[j:].index(item) + j
		# 		indices += [j]
		# 		j += 1
		# 	if t <= len(indices):
		# 		t = len(indices)
		# 		print(num)
		# 		for ind in indices:
		# 			print(inc[ind])
		# 			print(cor[ind])

	print(len(inc))

	for i,item in enumerate(inc):
		while (item in inc[i:]):
			index_to_remove = i + inc[i:].index(item)
			del inc[index_to_remove]
			del cor[index_to_remove]
		while (item in cor):
			index_to_remove = cor.index(item)
			del inc[index_to_remove]
			del cor[index_to_remove]
		if i%5000==0: print(i)

	print(len(inc), len(cor))
	inds = np.random.choice(len(inc),10)
	for ind in inds:
		print(inc[ind])
		print(cor[ind])

	output_dir = './wiki/'
	write_parallel_text(inc, cor, output_dir)



