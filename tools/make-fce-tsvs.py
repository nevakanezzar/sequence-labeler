import os
import sys

TARGET = "/home/skasewa/stuff/project/data/exp-data/train/fce/clc-fce-public-train-new.correct.tokenised.txt"
START=1000
END=220000
STEP=1000

command="python3 /home/skasewa/stuff/project/dev/create_many_tsv.py"

for i in range(START,END,STEP):
    name="fce-tsvs/fce"+str(i)
    source="fcepred"+str(i)+".txt"
    print(command,name,1,source,TARGET)


print("#",end='')
for i in range(END-STEP,START-STEP,-STEP):
    name="/cluster/project2/mr/skasewa/models/s2s-fce/corruptions/fce-tsvs/fce"+str(i)+".tsv,"
    print(name,end='')


