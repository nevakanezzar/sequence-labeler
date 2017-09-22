import sys
import os
import numpy as np

# TAKES ARGUMENTS filename tolerance

filename = sys.argv[1]
tol = int(sys.argv[2])
if len(sys.argv)>3:
    min_tol = int(sys.argv[3])
else:
    min_tol = 0

out_file = filename[:-4]+'-tol'+str(min_tol)+'-'+str(tol)+'.tsv'

num_files = int(sys.argv[4])


#### CODE BELOW HERE ISN'T FULLY IMPLEMENTED YET

class ED_TSV_File(object):
    """ A class to read, write, and analyse TSV files made for error detection """
    def __init__(self,input_file,major_label='i'):
        self.sent_list = list()
        self.sent_dict = dict()
        self.reverse_dict = dict()

        self.filename = input_file
        self.major_label = major_label
 
    def load_list(self):
        self.sent_list = list() #ensure scrubbing old data
        sent = ""
        labels = ""
        
        with open(self.filename,'r') as f:
            line = f.readline()
            while line:
                if line.strip() != "":
                    try:
                        word, label = line.strip().split('\t')
                    except:
                        print(".",line,".")
                        raise
                    sent += word+' '
                    labels += label
                else:
                    self.sent_list += [[sent.strip(),labels]]
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
                if line.strip() != "":
                    try:
                        word, label = line.strip().split('\t')
                    except:
                        print(".",line,".")
                        print(line.strip().split('\t'))
                        raise
                    sent += word+' '
                    labels += label
                else:
                    self.sent_dict[sent.strip()] = labels
                    sent = ""
                    labels = ""
                line = f.readline()
        return self.sent_dict

    def get_dict(self):
        if self.sent_dict == dict():
            return self.load_dict()
        else:
            return self.sent_dict


    def gen_reverse_dict(self):
        self.sent_dict = self.get_dict()
        self.reverse_dict = dict()
        for item in self.sent_dict:
            num_maj_lab = self.sent_dict[item].count(self.major_label)
            if num_maj_lab not in self.reverse_dict.keys():
                self.reverse_dict[num_maj_lab]=[[item,self.sent_dict[item]]]
            else:
                self.reverse_dict[num_maj_lab]+=[[item,self.sent_dict[item]]]
        return self.reverse_dict

    def get_reverse_dict(self):
        if self.reverse_dict == dict():
            return self.gen_reverse_dict()
        else:
            return self.reverse_dict

    def write_reverse_dict(self,out_file,min_tol,tol=-1):
        i = 0
        self.reverse_dict = self.get_reverse_dict()
        total_sents = 0
        skipped = 0
        with open(out_file,'w') as f:
            for i in self.reverse_dict.keys():
                if tol != -1 and (i > tol or i < min_tol):
                    continue

                write_string = ""
                for item in self.reverse_dict[i]:
                    sent = item[0].split()
                    labels = item[1]
                    if len(sent) != len(labels):
                        skipped += 1
                        continue
                    for token_num, token in enumerate(sent):
                        try:
                            write_string += token + "\t"+labels[token_num]+"\n"
                        except:
                            print(token, labels, token_num, sent)
                            raise
                    write_string += "\n"
                    total_sents += 1
                f.write(write_string)
        print("Wrote",total_sents,"sentences to",out_file)
        print("Skipped",skipped,"erroneous entries")
    
    def write_many(self, out_file,min_tol,tol=-1,num_files=1):
        i = 0
        self.reverse_dict = self.get_reverse_dict()
        total_sents = 0
        skipped = 0
        for i in self.reverse_dict.keys():
            if tol != -1 and (i > tol or i < min_tol):
                continue

            for item in self.reverse_dict[i]:
                
                write_string = ""

                sent = item[0].split()
                labels = item[1]
                if len(sent) != len(labels):
                    skipped += 1
                    continue
                for token_num, token in enumerate(sent):
                    try:
                        write_string += token + "\t"+labels[token_num]+"\n"
                    except:
                        print(token, labels, token_num, sent)
                        raise
                write_string += "\n"
                total_sents += 1
                with open(str(np.random.choice(num_files))+out_file,'a') as f:
                    f.write(write_string)
                    
        print("Wrote",total_sents,"sentences to",out_file)
        print("Skipped",skipped,"erroneous entries")
            


#### CODE ABOVE HERE ISN'T FULLY IMPLEMENTED HERE

tsv_file = ED_TSV_File(filename)
#tsv_list = tsv_file.get_list()
tsv_dict = tsv_file.get_dict()
tsv_revd = tsv_file.get_reverse_dict()
tsv_file.write_many(out_file,min_tol,tol,num_files)

#print(tsv_list[0:10])
#for i, key in enumerate(tsv_dict.keys()):
#    print(key,tsv_dict[key])
#    if i == 10:
#        break
#print(tsv_revd[3][0:10], len(tsv_revd[3]))
#
#print("Passed")

