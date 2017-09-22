#!/bin/python3

import sys
import os
import requests
from bs4 import BeautifulSoup
import time
import html
import re
import collections
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
INPUT_DIR = '../data/conll13-nucle-release2.3.1/original/data/'
INPUT_FIL = INPUT_DIR + 'official-preprocessed.m2'
OUTPUT_DIR = './conll13/'

DEBUG = False

#initialisations
inc_sents = []
cor_sents = []


with open(INPUT_FIL,'r') as in_file:
	while in_file:
		instance = []
		inc_temp = ''
		cor_temp = ''

		while True:
			x = in_file.readline()
			if not x: break
			if x is not '\n':
				instance+=[x.strip()]
			else:
				break
		for i, line in enumerate(instance):
			if i == 0:
				instance[i] = instance[i].split()[1:]
			else:
				instance[i] = instance[i].split("|||")
				instance[i][0] = instance[i][0].split()[1:]
				instance[i][0][0] = int(instance[i][0][0])
				instance[i][0][1] = int(instance[i][0][1])

		if not x: break
		# print(instance)
		sent = " ".join(instance[0])
		inc_temp = sent
		len_instance = len(instance)
		if len_instance == 1:
			cor_temp = sent
		else:
			inc_tokens = instance[0]
			cor_tokens = instance[0]
			offset = 0
			for i in range(len_instance-1,0,-1):
				# print(i)
				# print(instance[i])
				# print(cor_tokens)
				# if instance[i][1] == 'Um':
				# 	print("ALERT3!")
				# 	print(instance)
				# 	print(i)
				# 	print(cor_tokens)
				start_ann = instance[i][0][0]
				end_ann = instance[i][0][1]
				if start_ann == 0:
					beginning = []
				else:
					beginning = cor_tokens[0:start_ann]
				addition = [instance[i][2]]
				end = cor_tokens[end_ann:]
				cor_tokens = beginning + addition + end
				try:
					assert len(cor_tokens)>1
				except:
					print(instance)
				if (start_ann > end_ann):
					print("ALERT2!")
			cor_temp = " ".join(cor_tokens)
			# print(cor_sents[-1],"asdf")
		
		if not(cor_temp == '' or inc_temp == ''):
			inc_sents += [inc_temp]
			cor_sents += [cor_temp]

		# input()

print("\nSanity check, correct sentences:",len(cor_sents),"\tincorrect sentences:",len(inc_sents))
try:
	assert len(cor_sents) == len(inc_sents)
except:
	print("Sanity check FAILED!")
	raise AssertionError

write_parallel_text(inc_sents,cor_sents,OUTPUT_DIR)
