import os
import sys

if len(sys.argv)<2:
    print("Please provide txt file name to report statistics for")
    raise ValueError
else:
    TXTFILE = sys.argv[1]


num_sents = 0
vocab = set()
num_tokens = 0

#with open(TXTFILE,'r') as f:
#    line = f.readline()
#    while line:
#        num_sents += 1
#        tokens = line.strip().split()
#        vocab = vocab | set(tokens)
#        num_tokens += len(tokens)
#        line = f.readline()

with open(TXTFILE,'r') as f:
    file_all = f.read()
    num_sents = len(file_all.split('\n'))
    num_tokens = len(file_all.split(' '))
    file_all = file_all.replace('\n',' ')
    vocab = set(file_all.split(' '))


print("Sentences:\t",num_sents)
print("Tokens:\t",num_tokens)
print("Vocab:\t",len(vocab))


    
