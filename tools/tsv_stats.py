import sys
import os
import numpy as np




class ED_TSV_File(object):
    """ A class to read, write, and analyse TSV files made for error detection """
    def init(self,input_file,major_label='i'):
        self.sent_list = list()
        self.sent_dict = dict()
        self.filename = input_file
        self.major_label = major_label
 
    def load_list(self):
        self.sent_list = list() #ensure scrubbing old data
        sent = ""
        labels = ""
        
        with open(self.filename,'r') as f:
            line = f.readline()
            while line:
                if line != '\n':
                    word, label = line.strip().split('\t')
                    sent += word
                    labels += label
                else:
                    self.sent_list += [[sent,labels]]
                    sent = ""
                    labels = ""
                line = f.readline()
        return self.sent_list

    def get_list(self):
        if self.sent_list == []:
            return self.load_list()
        else:
            return self.sent_list


    def load_dict(self):
        self.sent_dict = dict() #ensure scrubbing old data
        sent = ""
        labels = ""
        
        with open(self.filename,'r') as f:
            line = f.readline()
            while line:
                if line != '\n':
                    word, label = line.strip().split()
                    sent += word
                    labels += label
                else:
                    self.sent_list[sent] = labels
                    sent = ""
                    labels = ""
                line = f.readline()
        return self.sent_dict

    def get_dict(self):
        if self.sent_dict == []:
            return self.load_dict()
        else:
            return self.sent_dict


    def gen_reverse_dict(self):
        self.sent_dict = self.get_dict()
        self.reverse_dict = dict()
        for item in self.sent_dict:
            num_maj_lab = self.sent_dict[item].count(self.major_label)
            if num_maj_lab not in self.reverse_dict:
                self.reverse_dict[num_maj_lab]=[item]
            else:
                self.reverse_dict[num_maj_lab]+=[item]
        
        
        self.sent_dict = dict() 
        self.filename = input_file

        sent = ""
        labels = ""
        wrong_count_sent = 0
        
        with open(self.filename,'r') as f:
            line = f.readline()
            while line:
                if line != '\n':
                    word, label = line.strip().split()
                    sent += word
                    labels += label
                    token_count += 1
                    if label == 'i':
                        wrong_count += 1
                        wrong_count_sent += 1
                else:
                    sents[sent] = [labels, len(labels), wrong_count_sent]
                    if wrong_count_sent not in wrong_count_dict:
                        wrong_count_dict[wrong_count_sent] = 1
                    else:
                        wrong_count_dict[wrong_count_sent] += 1
                    sent = ""
                    labels = ""
                    wrong_count_sent = 0
                    sent_count += 1
                line = f.readline()
        




wrong_count_dict = dict()
sents = dict()
token_count = 0
wrong_count  = 0
sent_count = 0

sent = ""
labels = ""
wrong_count_sent = 0

input_file = sys.argv[1]

with open(input_file,'r') as f:
    line = f.readline()
    while line:
        if line != '\n':
            try:
                word, label = line.strip().split('\t')
                sent += word
                labels += label
                token_count += 1
                if label == 'i':
                    wrong_count += 1
                    wrong_count_sent += 1
            except:
                print("Skipped this:",line)
                line = f.readline()
                continue
        elif sent != "":
            sents[sent] = [labels, len(labels), wrong_count_sent]
            if wrong_count_sent not in wrong_count_dict:
                wrong_count_dict[wrong_count_sent] = 1
            else:
                wrong_count_dict[wrong_count_sent] += 1
            sent = ""
            labels = ""
            wrong_count_sent = 0
            sent_count += 1
        line = f.readline()


print("Sentences:",sent_count)
print("Tokens:", token_count)
print("Wrong tokens:",wrong_count,"\tPercentage:",wrong_count/token_count)

max_wrong = -1
min_wrong = 999
max_len = -1
min_len = 999

dist_mistake_percent = []
dist_num_mistakes = []

for key in sents:
    item = sents[key]

    if item[1] > max_len:
        max_len = item[1]
    elif min_len > item[1]:
        min_len = item[1]

    if item[2] > max_wrong:
        max_wrong = item[2]
    elif min_wrong > item[2]:
        min_wrong = item[2]
    try:
        dist_mistake_percent += [item[2]/item[1]]
    except:
        print(key,item)
    dist_num_mistakes += [item[2]]


print("Max sent len:", max_len, "\tmin sent len:",min_len)
print("Max wrong:", max_wrong,"\tmin wrong:",min_wrong)


wrong_count_np = np.zeros([max(wrong_count_dict)+1,4])
print(wrong_count_dict)
for item in wrong_count_dict:
    wrong_count_np[item][0:2] = [item,wrong_count_dict[item]]

wrong_count_np[:,2]=wrong_count_np[:,1]/sum(wrong_count_np[:,1])
wrong_count_np[0,3]=wrong_count_np[0,2]

for i in range(1,int(wrong_count_np[-1,0])+1):
    wrong_count_np[i,3] = wrong_count_np[i,2] + wrong_count_np[i-1,3]

#wrong_count_np = wrong_count_np[wrong_count_np[:,0].argsort()]


print(wrong_count_np)


bins = 20
l = len(dist_mistake_percent)
dist_mistake_percent.sort()

print("\nhistogram of % mistakes")
for bin, i in enumerate(range(0, l, int(l/bins))):
    print(bin, i, np.average(dist_mistake_percent[i:i+int(l/bins)]))


l = len(dist_num_mistakes)

dist_num_mistakes.sort()
print("\nhistogram of num mistakes")
for i in range(0, l, int(l/bins)):
    print(i, np.average(dist_num_mistakes[i:i+int(l/bins)]))

