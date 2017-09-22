#!/bin/python3

import sys
import os
import time
import html
import re
import collections
import numpy as np
from sent_align import get_alignment 


#CONSTANTS
INPUT_DIR = './wiki/'
INPUT_SOURCES = INPUT_DIR + 'sources.txt'
INPUT_TARGETS = INPUT_DIR + 'targets.txt'

OUTPUT_DIR = './wiki/'
OUTPUT_TRAIN = OUTPUT_DIR + 'wikierrorcorpus.train.tsv'
OUTPUT_DEV = OUTPUT_DIR + 'wikierrorcorpus.dev.tsv'
OUTPUT_TEST = OUTPUT_DIR + 'wikierrorcorpus.test.tsv'

SEED = np.random.seed(42)   # the answer is a good place to begin
DEV_THRESHOLD = 0.7
TEST_THRESHOLD = 0.85 # 15% dev, and 15% test

DEBUG = False

with open(INPUT_SOURCES,'r',encoding='utf-8') as source_file:
	with open(INPUT_TARGETS,'r',encoding='utf-8') as target_file:
		while True:
			correct = target_file.readline().strip()
			wrong = source_file.readline().strip()
			if not correct: break
			if not wrong: break

			align = get_alignment(correct,wrong)
			p = np.random.random()
			if p < DEV_THRESHOLD:
				write_file = OUTPUT_TRAIN
			elif p > TEST_THRESHOLD:
				write_file = OUTPUT_TEST
			else:
				write_file = OUTPUT_DEV
			with open(write_file,'a', encoding='utf-8') as output_file:
				for token in align:
					write_token = token[0]+'\t'+token[1]+'\n'
					output_file.write(write_token)
				output_file.write('\n')

			




