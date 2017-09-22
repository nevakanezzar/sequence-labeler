import os
import sys

LOC = '/home/skasewa/stuff/project/data/parsed_fce/train/'

VOCAB_SOURCE = LOC + 'vocab.sources.txt'
VOCAB_TARGET = LOC + 'vocab.targets.txt'
VOCAB_CHAR_SOURCE = LOC + 'vocab.sources.char.txt'
VOCAB_CHAR_TARGET = LOC + 'vocab.targets.char.txt'

OUT_VOCAB = LOC + 'vocab.combined.txt'
OUT_VOCAB_CHAR = LOC + 'vocab.combined.char.txt'


char_vocab = set()

with open(VOCAB_CHAR_SOURCE,'r') as f:
    x = f.readline()
    while x:
        char_vocab.add(x.strip())
        x = f.readline()

with open(VOCAB_CHAR_TARGET,'r') as f:
    x = f.readline()
    while x:
        char_vocab.add(x.strip())
        x = f.readline()

print(char_vocab)

with open(OUT_VOCAB_CHAR,'w') as f:
    while True:
        if len(char_vocab)==0:
            break
        y = char_vocab.pop()
        f.write(y+'\n')

print("script incomplete!")
raise 
