#!/bin/python3

import sys
import os
import time
import html
import re
import collections
import numpy as np
from sent_align import get_alignment 

if len(sys.argv) > 1:
	OF_PREFIX = sys.argv[1]			#OF = OUTPUTFILE
else:
	OF_PREFIX = './wiki/wikierrorcorpus'

if len(sys.argv) > 2:
	N_FILES = int(sys.argv[2])			#NUMBER OF FILES TO CREATE
else:
	N_FILES = 10

if len(sys.argv) > 3:
 	INPUT_SOURCES = sys.argv[3]			#INPUT SOURCES
else:
	INPUT_SOURCES = './wiki/sources.txt'

if len(sys.argv) > 4:
 	INPUT_TARGETS = sys.argv[4]			#INPUT TARGETS
else:
	INPUT_TARGETS = './wiki/targets.txt'


if N_FILES == 1:
	write_file = OF_PREFIX+'.tsv'


DEBUG = True
last_token = ''

with open(INPUT_SOURCES,'r',encoding='utf-8') as source_file:
	with open(INPUT_TARGETS,'r',encoding='utf-8') as target_file:
		while True:
			correct = target_file.readline()
			wrong = source_file.readline()
			if (not correct) and (not wrong):
				break
			correct = correct.strip()
			wrong = wrong.strip()

			align = get_alignment(correct,wrong)
			if N_FILES != 1:
				write_file = OF_PREFIX+str(np.random.randint(0,N_FILES))+'.tsv'

			with open(write_file,'a', encoding='utf-8') as output_file:

				write_token = ''
				for token in align:
					write_token = write_token + token[0]+'\t'+token[1]+'\n'

				output_file.write(write_token)
				output_file.write('\n')

			




