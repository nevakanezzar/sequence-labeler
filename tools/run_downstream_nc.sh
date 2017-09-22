#!/bin/bash

# expects $1 as source file, $2 as target file, $3 as tsv to create, $4 as GPU number
# creates 1 tsv $3
# appends fce-error-detection/tsv/fce-public.train.original.tsv
# runs sequence-labeling experiment on this tsv

python3 create_many_tsv.py $3 1 $1 $2

FINAL="fce_$3"
TSV1="$3.tsv"
TSV_FILE="$FINAL.tsv"
echo $TSV_FILE
cat ../data/fce-error-detection/tsv/fce-public.train.original.tsv $TSV1 > $TSV_FILE

cd ../seqlab/sequence-labeler/
echo $PWD

MODEL_FILE="$FINAL.model"
CONF_FILE="$FINAL.conf"
RESULT_FILE="$FINAL.results"

cat > $CONF_FILE <<EOF
[config]
path_train = /home/skasewa/stuff/project/dev/$TSV_FILE
path_dev = /home/skasewa/stuff/project/seqlab/data/fce-public.dev.original.tsv
path_test = /home/skasewa/stuff/project/seqlab/data/fce-public.dev.original.tsv:/home/skasewa/stuff/project/seqlab/data/fce-public.test.original.tsv:/home/skasewa/stuff/project/dev/conll14-test1/conll14-test1.tsv:/home/skasewa/stuff/project/dev/conll14-test2/conll14-test2.tsv
main_label = i
conll_eval = False
preload_vectors = /home/skasewa/stuff/project/data/googlenews-vectors/GoogleNews-vectors-negative300.txt
word_embedding_size = 300
char_embedding_size = 50
word_recurrent_size = 200
char_recurrent_size = 200
narrow_layer_size = 50
best_model_selector = dev_f05:high
epochs = 100
stop_if_no_improvement_for_epochs = 10
learningrate = 1.0
min_word_freq = 1
max_batch_size = 256
save = /home/skasewa/stuff/project/models/3_nc/$MODEL_FILE
load = 
random_seed = 42
crf_on_top = True
char_integration_method = attention
EOF

THEANO_FLAGS="device=gpu$4,floatX=float32" python2 sequence_labeling_experiment.py $CONF_FILE > $RESULT_FILE