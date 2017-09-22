#!/bin/python3

import sys
import os
from nltk.tokenize import wordpunct_tokenize


#CONSTANTS
INPUT_DIR = './evp/'
INPUT_FIL = INPUT_DIR + 'evpcorpus.txt'

OUTPUT_DIR = './evp/'
OUTPUT_FIL = OUTPUT_DIR + 'evpcorpus_fixed.txt'

collected_sents = []

with open(INPUT_FIL, "r") as source_file:
	line = source_file.readline()
	while line:
		collected_sents += [" ".join(wordpunct_tokenize(line.strip()))+'\n']
		line = source_file.readline()

with open(OUTPUT_FIL,'w') as output_file:
	for record in collected_sents:
		output_file.write(record)

print("Wrote {}".format(OUTPUT_FIL))	


