#!/bin/python3

#requires nltk (with punkt?) for tokenization

from nltk.tokenize import wordpunct_tokenize
import numpy as np


max_sent_len = 200 + 1 #max number of tokens + 1
p_gap = 1.0
p_mismatch = 1.5
p_static = np.zeros([max_sent_len,max_sent_len])
for i in range(max_sent_len):
	p_static[0,i] = i * p_gap
	p_static[i,0] = i * p_gap


def get_alignment(correct,wrong):

	alignment = []
	cor_mod = []
	wro_mod = []
	gap = "<gap>"
	
	c_tokens = wordpunct_tokenize(correct)
	c_len = len(c_tokens) + 1  #using 1-indexing

	if c_len > max_sent_len:  #truncate if too long
		c_len = max_sent_len
		c_tokens = c_tokens[:max_sent_len-1]
	
	w_tokens = wordpunct_tokenize(wrong)
	w_len = len(w_tokens) + 1 	#using 1-indexing

	if w_len > max_sent_len:  #truncate if too long
		w_len = max_sent_len
		w_tokens = w_tokens[:max_sent_len-1]

	penalties = np.array(p_static[0:c_len,0:w_len])  #make a copy of starting state
	for i in range(1,c_len):
		for j in range(1,w_len):
			if c_tokens[i-1] == w_tokens[j-1]:
				p_ij = 0
			else:
				p_ij = p_mismatch
			try:
				penalties[i,j] = min(penalties[i-1,j-1] + p_ij,
								penalties[i,j-1] + p_gap,
								penalties[i-1,j] + p_gap)
			except:
				print(correct, wrong)
				raise

	i = c_len-1
	j = w_len-1
	
	while i > 0 and j > 0:
		if penalties[i,j] == penalties[i,j-1] + p_gap:
			wro_mod += [w_tokens[j-1]]
			cor_mod += [gap]
			j = j-1
		elif penalties[i,j] == penalties[i-1,j] + p_gap:
			wro_mod += [gap]
			cor_mod += [c_tokens[i-1]]
			i = i-1
		else:
			wro_mod += [w_tokens[j-1]]
			cor_mod += [c_tokens[i-1]]
			i = i-1
			j = j-1

	wro_mod.reverse()
	cor_mod.reverse()

	if i > 0:
		wro_mod=[gap]*i+wro_mod
		cor_mod=c_tokens[0:i]+cor_mod
	elif j > 0:
		cor_mod=[gap]*j+cor_mod
		wro_mod=w_tokens[0:j]+wro_mod
	
	# print(wro_mod)
	# print(cor_mod)
	# print(len(wro_mod),len(cor_mod))

	wro_gap_flag = False
	for i,wro_token in enumerate(wro_mod):
		cor_token = cor_mod[i]
		if cor_token == gap:
			alignment+=[[wro_token,'i']]
		elif wro_token == gap:
			wro_gap_flag = True
			continue
		elif wro_token == cor_token:
			if wro_gap_flag == True:
				alignment+=[[wro_token,'i']]
				wro_gap_flag = False
			else:
				alignment+=[[wro_token,'c']]
		else:
			alignment+=[[wro_token,'i']]

	if wro_gap_flag == True:
		alignment[-1][1] = 'i'

	return alignment


if __name__ == '__main__':  #acts as a test

	wrong_sents= ["\"The Wurst of P. D. Q. Bach\", collection of works by Peter Schickele under his comic pseudonym of P. D. Q. Bach originally recorded on the Vanguard Records label by the composer.","\"Popoyo\" is a small beach town in the Tola municipality of Rivas Department of Nicaragua.","In addition for the hotel, there is also an administrative building and a housing center for the stadium's workers with a total capacity of 80 people (total area is 3500 square meters).","A B C D E F G","A B C D E F","C D E","A B E F","A B C D E F G","A B C D E F G","A B C D E"]
	correct_sents =["\"The Wurst of P. D. Q. Bach\" is a collection of works by Peter Schickele under his comic pseudonym of P. D. Q. Bach originally recorded on the Vanguard Records label by the composer.","\"Popoyo\" is a small beach town in the Tola municipality of the Rivas Department of Nicaragua.","In addition for the hotel, there is also an administrative building and a housing centre for the stadium's workers with a total capacity of 80 people (total area is 3500 square meters).","A B C D E F","A B C D E F G","A B C D E F G","A B C D E F G","C D E","A B E F","A B G D E"]


	for i,w_sent in enumerate(wrong_sents):
		c_sent = correct_sents[i]
		print(c_sent, '<-',w_sent)
		print(get_alignment(c_sent,w_sent))
