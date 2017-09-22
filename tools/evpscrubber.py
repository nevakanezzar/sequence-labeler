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


#CONSTANTS
OUTPUT_DIR = './evp/'
OUTPUT_FIL = OUTPUT_DIR + 'evpcorpus.txt'
EVP_URL = "http://vocabulary.englishprofile.org"
DIC_PATH ="/dictionary/word-list/uk/a1_c2/"
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

DEBUG = False

#initialisations
collected_sents = []

for letter in LETTERS:
	print("\n\n\n\n\n ----------",letter," ----------\n\n\n\n\n")
	r1 = requests.get(EVP_URL+DIC_PATH+letter, auth=('englishprofile','vocabulary'))

	if r1.status_code != requests.codes.ok:
		print("Error 51605: get",r1.url,"failed, status code",r1.status_code)

	r1soup = BeautifulSoup(r1.text,'lxml')
	results = r1soup.find_all("li")

	for block in results:
		list_path = block.a['href']
		# print(list_path)
		
		r2 = requests.get(EVP_URL+list_path, auth=('englishprofile','vocabulary'))
		
		if r2.status_code != requests.codes.ok:
			print("Error 51605: get",r2.url,"failed, status code",r2.status_code)

		r2soup = BeautifulSoup(r2.text,'lxml')
		words = r2soup.find_all("li")
		word_path_set = set()
		for block in words:
			string = block.a['href']
			index = string.find('#')
			word_path_set.add(string[:index+1])
		# print(word_path_set)
		for word_path in word_path_set:
			r3 = requests.get(EVP_URL+word_path, auth=('englishprofile','vocabulary'))
		
			if r3.status_code != requests.codes.ok:
				print("Error 51605: get",r3.url,"failed, status code",r3.status_code)

			r3soup = BeautifulSoup(r3.text,'lxml')
			# print(EVP_URL+word_path)
			# print(r3soup)
			offset = len("Learner example: ")
			for start in re.finditer("Learner example:", r3soup.text):
				start_ind = start.start() + offset
				end_ind = next(re.finditer(r"[!.?]",r3soup.text[start_ind:])).start() + start_ind + 1
				sent = r3soup.text[start_ind:end_ind]
				sent = sent.translate({ord('['):None,ord(']'):None})
				collected_sents += [sent.strip()]
				print(collected_sents[-1])

print("Collected ",len(collected_sents),"sentences")

with open(OUTPUT_FIL, "w") as source_file:
	for record in collected_sents:
		record_corrected = " ".join(wordpunct_tokenize(record))
		source_file.write(record_corrected + "\n")

print("Wrote {}".format(OUTPUT_FIL))	


