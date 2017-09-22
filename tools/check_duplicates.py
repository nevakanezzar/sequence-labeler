import os
import sys


#main_file = '/home/skasewa/stuff/project/data/exp-data/train/lang8/lang8-train-fce.tsv'
#main_file = '/home/skasewa/stuff/project/data/wiked/tmp/wiki-roman-large.tsv'
main_file = '/home/skasewa/stuff/project/data/exp-data/train/lang8/lang8-train.tsv'

comparison_files = ['/home/skasewa/stuff/project/data/exp-data/dev/fce/fce-public.dev.original.tsv',
                    '/home/skasewa/stuff/project/data/exp-data/test/fce/fce-public.test.original.tsv',
                    '/home/skasewa/stuff/project/data/exp-data/test/conll14-test0/nucle.test0.original.tsv',
                    '/home/skasewa/stuff/project/data/exp-data/test/conll14-test1/nucle.test1.original.tsv',
                    '/home/skasewa/stuff/project/data/exp-data/test/lang8/lang8-test.tsv',
                    '/cluster/project2/mr/skasewa/models/1layer-s2s-fce/corruptions/lang8c-fce-tol1.tsv'
                    ]


def load_sents_from_tsv(filename):
    sent_dict = dict()

    with open(filename,'r') as f:
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

    return sent_dict

main_sents = load_sents_from_tsv(main_file)
main_sents_set = set(main_sents.keys())

for file1 in comparison_files:
    comparison_sents = load_sents_from_tsv(file1)
    comparison_set = set(comparison_sents.keys())
    common_sents = main_sents_set & comparison_set
    print("Sentences common between main file and ",file1,":",len(common_sents),"/",len(comparison_set))
    #print(common_sents)

