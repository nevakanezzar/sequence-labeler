import os
import sys

FILE = sys.argv[1]
code = sys.argv[2]


mults = [0.11111111, 0.25, 0.4825, 0.6666666, 1, 1.5, 2.33333333, 4, 9]


# file 0

conf_file_content = ["[config]",
                     "path_train = "+FILE,
                      "multiple = 1",
                     "path_dev = /home/skasewa/stuff/project/data/exp-data/dev/fce/fce-public.dev.original.tsv",
                     "path_test = /home/skasewa/stuff/project/data/exp-data/dev/fce/fce-public.dev.original.tsv:/home/skasewa/stuff/project/data/exp-data/test/fce/fce-public.test.original.tsv:/home/skasewa/stuff/project/data/exp-data/test/conll14-test0/nucle.test0.original.tsv:/home/skasewa/stuff/project/data/exp-data/test/conll14-test1/nucle.test1.original.tsv:/home/skasewa/stuff/project/data/exp-data/test/lang8/lang8-test.tsv",
                     "main_label = i",
                     "conll_eval = False",
                     "lowercase_words = True",
                     "lowercase_chars = False",
                     "replace_digits = True",
                     "min_word_freq = 1",
                     "use_singletons = False",
                     "allowed_word_length = -1",
                     "preload_vectors = /home/skasewa/stuff/project/data/googlenews-vectors/GoogleNews-vectors-negative300.txt",
                     "word_embedding_size = 300",
                     "char_embedding_size = 50",
                     "word_recurrent_size = 200",
                     "char_recurrent_size = 200",
                     "narrow_layer_size = 50",
                     "dropout_input = 0.5",
                     "best_model_selector = dev_f05:high",
                     "epochs = 100",
                     "stop_if_no_improvement_for_epochs = 20",
                     "learningrate = 1.0",
                     "opt_strategy = adadelta",
                     "max_batch_size = 256",
                     "save = /home/skasewa/stuff/project/models/downstream/"+code+"0.model",
                     "load = ",
                     "random_seed = 420",
                     "crf_on_top = False",
                     "char_integration_method = attention",
                     "garbage_collection = False",
                     "lmcost_gamma = 0.1",
                     "lmcost_layer_size = 50",
                     "lmcost_max_vocab_size = 10000",
                     ]

with open(code+"0.conf", 'w') as f:
    f.write("\n".join(conf_file_content))


# files 1-9

for i, mult in enumerate(mults):
    batch_size = 512 if i<7 else 128
    conf_file_content = ["[config]",
                         "path_train = /home/skasewa/stuff/project/data/exp-data/train/fce/fce-public.train.original.tsv,"+FILE,
                         "multiple = "+str(mult),
                         "path_dev = /home/skasewa/stuff/project/data/exp-data/dev/fce/fce-public.dev.original.tsv",
                         "path_test = /home/skasewa/stuff/project/data/exp-data/dev/fce/fce-public.dev.original.tsv:/home/skasewa/stuff/project/data/exp-data/test/fce/fce-public.test.original.tsv:/home/skasewa/stuff/project/data/exp-data/test/conll14-test0/nucle.test0.original.tsv:/home/skasewa/stuff/project/data/exp-data/test/conll14-test1/nucle.test1.original.tsv:/home/skasewa/stuff/project/data/exp-data/test/lang8/lang8-test.tsv",
                         "main_label = i",
                         "conll_eval = False",
                         "lowercase_words = True",
                         "lowercase_chars = False",
                         "replace_digits = True",
                         "min_word_freq = 1",
                         "use_singletons = False",
                         "allowed_word_length = -1",
                         "preload_vectors = /home/skasewa/stuff/project/data/googlenews-vectors/GoogleNews-vectors-negative300.txt",
                         "word_embedding_size = 300",
                         "char_embedding_size = 50",
                         "word_recurrent_size = 200",
                         "char_recurrent_size = 200",
                         "narrow_layer_size = 50",
                         "dropout_input = 0.5",
                         "best_model_selector = dev_f05:high",
                         "epochs = 50",
                         "stop_if_no_improvement_for_epochs = 10",
                         "learningrate = 1.0",
                         "opt_strategy = adadelta",
                         "max_batch_size = "+str(batch_size),
                         "save = /home/skasewa/stuff/project/models/downstream/"+code+str(i+1)+".model",
                         "load = ",
                         "random_seed = 420",
                         "crf_on_top = False",
                         "char_integration_method = attention",
                         "garbage_collection = False",
                         "lmcost_gamma = 0.1",
                         "lmcost_layer_size = 50",
                         "lmcost_max_vocab_size = 10000",
                         ]

    with open(code+str(i+1)+".conf", 'w') as f:
        f.write("\n".join(conf_file_content))
