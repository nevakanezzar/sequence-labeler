#!/bin/bash

export THEANO_FLAGS='device=gpu1,floatX=float32'

export CODE='lm'
#python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}0.conf > ${CODE}0.results
#python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}1.conf > ${CODE}1.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}2.conf > ${CODE}2.results
#python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}3.conf > ${CODE}3.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}4.conf > ${CODE}4.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}5.conf > ${CODE}5.results
