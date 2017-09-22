import collections
import os
import sys
import numpy

if len(sys.argv)==1:
    INPUT_FILE = 'wiki/wikierrorcorpus.train.tsv'
else:
    INPUT_FILE = sys.argv[1]

total_words = 0
tokens = collections.Counter()
classes = collections.Counter()
unique_chars = collections.Counter()
sents = 0

with open(INPUT_FILE,'r') as f:
    for line in f:
        input_line = line.strip()
        input_line = input_line.split('\t')
        if len(input_line)==1:
            sents+=1
            continue
        tokens[input_line[0]]+=1
        classes[input_line[1]]+=1
        unique_chars.update(collections.Counter(input_line[0]))
        #print(input_line,input_line[0], input_line[1])
        #input()

print("Stats for file:",INPUT_FILE)
print("Sentences:",sents)
print("Tokens:",sum(tokens.values()))
print("Unique tokens:",len(tokens))
print("Classes:",classes)
print("Unique characters:",len(unique_chars))
#print("Characters:",unique_chars)

# print characters with less than 300 counts as a list
# char_list = []
# for key in unique_chars.keys():
#     if unique_chars[key] < 300:
#         char_list += [key]
# print(char_list)
