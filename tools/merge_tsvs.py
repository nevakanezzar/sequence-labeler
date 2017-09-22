import os
import sys

if ":" in sys.argv[1]:
    files = sys.argv[1].split(":")
    outfile = sys.argv[2]

else:
    files = [sys.argv[1]+str(i)+sys.argv[5] for i in range(int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))]
    outfile = sys.argv[6]


sent_dict = dict()

for item in files:
    with open(item,'r') as f:
        line = f.readline()
        sent = ""
        labels = ""
        while line:
            if line.strip() != '':
                word,label = line.strip().split('\t')
                sent += word + ' '
                labels += label
            else:
                sent_dict[sent.strip()]=labels
                sent = ""
                labels = ""
            line = f.readline()
    print("Sents so far:",len(sent_dict))

print("Total:",len(sent_dict))

with open(outfile,'w') as f:
    for item in sent_dict:
        sent_tokens = item.split()
        label = sent_dict[item]
        assert len(sent_tokens) == len(label)
        for i,token in enumerate(sent_tokens):
            f.write(token+'\t'+label[i]+'\n')
        f.write('\n')

print("Wrote:",outfile)
