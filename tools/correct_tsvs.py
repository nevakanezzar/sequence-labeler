import os
import sys

correct_txt = sys.argv[1]
if correct_txt[-3:]=='txt':
    correct_tsv = correct_txt[:-3]+'tsv'
else:
    sys.exit(1)

print(correct_txt,"to",correct_tsv)

write_data = ""
with open(correct_txt,'r') as f:
    line = f.readline()
    while line:
        tokens = line.strip().split()
        for token in tokens:
             write_data += token+"\tc\n"
        write_data += "\n"
        line = f.readline()

with open(correct_tsv,'w') as f2:
    f2.write(write_data)

