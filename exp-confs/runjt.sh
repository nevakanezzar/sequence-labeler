#!/bin/bash

#export CODE='g'
#export THEANO_FLAGS='device=gpu2,floatX=float32'
#python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}0.conf > ${CODE}0.results
#python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}0a.conf > ${CODE}0a.results
#python ../sequence-labeler-master/v2_sle_mixeddata.py ${CODE}1.conf > ${CODE}1.results
#python ../sequence-labeler-master/v2_sle_mixeddata.py ${CODE}2.conf > ${CODE}2.results
#python ../sequence-labeler-master/v2_sle_mixeddata.py ${CODE}3.conf > ${CODE}3.results
#python ../sequence-labeler-master/v2_sle_mixeddata.py ${CODE}4.conf > ${CODE}4.results
#python ../sequence-labeler-master/v2_sle_mixeddata.py ${CODE}5.conf > ${CODE}5.results
#python ../sequence-labeler-master/v2_sle_mixeddata.py ${CODE}6.conf > ${CODE}6.results
#python ../sequence-labeler-master/v2_sle_mixeddata.py ${CODE}7.conf > ${CODE}7.results
#python ../sequence-labeler-master/v2_sle_mixeddata.py ${CODE}8.conf > ${CODE}8.results
#python ../sequence-labeler-master/v2_sle_mixeddata.py ${CODE}9.conf > ${CODE}9.results

export THEANO_FLAGS='device=gpu1,floatX=float32'

export CODE='j'
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}0.conf > ${CODE}0.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}0a.conf > ${CODE}0a.results

export CODE='k'
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}0.conf > ${CODE}0.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}0a.conf > ${CODE}0a.results

export CODE='l'
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}0.conf > ${CODE}0.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}0a.conf > ${CODE}0a.results

export CODE='m'
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}0.conf > ${CODE}0.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}0a.conf > ${CODE}0a.results

export CODE='n'
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}0.conf > ${CODE}0.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}0a.conf > ${CODE}0a.results

export CODE='o'
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}0.conf > ${CODE}0.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}0a.conf > ${CODE}0a.results

export CODE='p'
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}0.conf > ${CODE}0.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}0a.conf > ${CODE}0a.results

export CODE='q'
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}0.conf > ${CODE}0.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}0a.conf > ${CODE}0a.results

export CODE='r'
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}0.conf > ${CODE}0.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}0a.conf > ${CODE}0a.results

export CODE='s'
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}0.conf > ${CODE}0.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}0a.conf > ${CODE}0a.results

export CODE='t'
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}0.conf > ${CODE}0.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}0a.conf > ${CODE}0a.results

