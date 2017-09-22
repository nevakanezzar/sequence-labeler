import os
import sys

START = 100000
END = 110000 #not inclusive
STEP = 1000

FILE = 'fce'
EXT = '.tsv'

sent_dict = dict()
total_sents = 0
kept_sents = 0
sent = ''
sent_labels = ''

DEBUG = True


for i in range(START,END,STEP):
    FILENAME = FILE+str(i)+EXT
    with open(FILENAME,'r') as f:
        if DEBUG:
            print("Processing file:",FILENAME)
        sent = ""
        line = f.readline()
        while line:
            line_split = line.strip().split('\t')
            if DEBUG:
                print(line_split)
                input()
            if line_split == ['']:
                total_sents += 1
                sent_dict[sent.strip()]=sent_labels
                sent = ""
                sent_labels = ""
                line = f.readline()
                continue
            token = line_split[0]
            label = line_split[1]
            sent += token + ' '
            sent_labels += label
            line = f.readline()

print("Total sentences:",total_sents)

for key in sent_dict:
    kept_sents += 1

print("Kept sentences:",kept_sents)
