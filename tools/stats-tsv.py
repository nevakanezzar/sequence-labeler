import os
import sys

if len(sys.argv)<2:
    print("Please provide tsv file name to report statistics for")
    raise ValueError
else:
    TSVFILE = sys.argv[1]


num_sents = 0
vocab = set()
num_tokens = 0

with open(TSVFILE,'r') as f:
    line = f.readline()
    while line:
        if line == '\n':num_sents += 1
        else: num_tokens += 1
        vocab.add(line)
        line = f.readline()

print("Sentences:\t",num_sents)
print("Tokens:\t",num_tokens)
print("Vocab:\t",len(vocab))


    
