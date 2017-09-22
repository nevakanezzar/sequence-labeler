#!/bin/bash

export THEANO_FLAGS='device=gpu2,floatX=float32'

export CODE='lc2a-tol'
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}1.conf > ${CODE}1.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}3.conf > ${CODE}3.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}5.conf > ${CODE}5.results

export CODE='lc2-tol'
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}1.conf > ${CODE}1.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}3.conf > ${CODE}3.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}5.conf > ${CODE}5.results
