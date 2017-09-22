import os
import sys

original_wrong_list = []

#original_file = 'fce-train-aligned.tsv'
#true_file = '/home/skasewa/stuff/project/data/exp-data/train/fce/fce-public.train.original.tsv'

original_file = '/home/skasewa/stuff/project/data/exp-data/train/lang8/lang8-train.tsv'
true_file = '/home/skasewa/stuff/project/data/exp-data/train/lang8/lang8-train.tsv'

tol = int(sys.argv[1])
#outfile = 'told-fce-merged-'+str(tol)+'.tsv'
outfile = '/cluster/project2/mr/skasewa/models/1layer-small-s2s-fce-lang8/corruptions/lang8c2-tol'+str(tol)+'.tsv'

start = 101000
end = 102000
step = 1000
#pref = '/cluster/project2/mr/skasewa/models/1layer-s2s-fce/corruptions/fcec-'
pref = '/cluster/project2/mr/skasewa/models/1layer-small-s2s-fce-lang8/corruptions/lang8c2-'
suf = '.tsv'
files = []

for i in range(start,end,step):
    files += [pref+str(i)+suf]

sent_dict = dict()

with open(original_file,'r') as f:
    line = f.readline()
    sent = ""
    labels = ""
    while line:
        if line != '\n':
            word,label = line.strip().split('\t')
            sent += word + ' '
            labels += label
        else:
            original_wrong_list += [[sent.strip(),labels]]
            #sent_dict[sent.strip()]=labels
            sent = ""
            labels = ""
        line = f.readline()
#print("Sents in original:",len(sent_dict))
#print(original_wrong_list[0:3])
total_index = len(original_wrong_list)

for item in files:
    try:
        with open(item,'r') as f:
            line = f.readline()
            index = 0
            sent = ""
            labels = ""
            while index<total_index:
                if line != '\n':
                    word,label = line.strip().split('\t')
                    sent += word + ' '
                    labels += label
                else:
                    sent = sent.strip()
                    wrong_label_count = sum([1 for i in labels if i == 'i'])
                    try:
                        wrong_label_count_original = sum([1 for i in original_wrong_list[index][1] if i == 'i'])
                    except:
                        print(index, len(original_wrong_list))
                        raise
                    if sent!=original_wrong_list[index][0] and abs(wrong_label_count - wrong_label_count_original) < tol:
                        sent_dict[sent]=labels
                        #print(sent, labels, original_wrong_list[index])
                    sent = ""
                    labels = ""
                    index += 1
                line = f.readline()
        print("File:",item,"\tSents so far:",len(sent_dict))
    except:
        print("Failed on file",item,"\tContinuing...")
        continue

with open(true_file, 'r') as f:
    line = f.readline()
    sent = ""
    labels = ""
    while line:
        if line != '\n':
            word,label = line.strip().split('\t')
            sent += word + ' '
            labels += label
        else:
            sent = sent.strip()
            sent_dict[sent]=labels
            sent = ""
            labels = ""
        line = f.readline()

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
