#!/bin/bash

export THEANO_FLAGS='device=gpu2,floatX=float32'

export CODE='lc1'
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}.conf > ${CODE}.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}a.conf > ${CODE}a.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}a-tol1.conf > ${CODE}a-tol1.results

export CODE='lc2'
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}.conf > ${CODE}.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}a.conf > ${CODE}a.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}a-tol1.conf > ${CODE}a-tol1.results
