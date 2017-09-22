#!/bin/bash

export THEANO_FLAGS='device=gpu1,floatX=float32'

export CODE='tol'
# python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}1.conf > ${CODE}1.results
# python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}2.conf > ${CODE}2.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}3.conf > ${CODE}3.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}4.conf > ${CODE}4.results
# python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}5.conf > ${CODE}5.results

export CODE='tola'
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}1.conf > ${CODE}1.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}2.conf > ${CODE}2.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}3.conf > ${CODE}3.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}4.conf > ${CODE}4.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}5.conf > ${CODE}5.results

export CODE='tolb'
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}1.conf > ${CODE}1.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}2.conf > ${CODE}2.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}3.conf > ${CODE}3.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}4.conf > ${CODE}4.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}5.conf > ${CODE}5.results


