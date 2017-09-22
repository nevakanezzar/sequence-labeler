#!/bin/bash

export CODE='lc1-short'
export THEANO_FLAGS='device=gpu1,floatX=float32'
#python ../sequence-labeler-master/v2_sle_mixeddata.py ${CODE}1.conf > ${CODE}1.results
#python ../sequence-labeler-master/v2_sle_mixeddata.py ${CODE}2.conf > ${CODE}2.results
#python ../sequence-labeler-master/v2_sle_mixeddata.py ${CODE}3.conf > ${CODE}3.results
#python ../sequence-labeler-master/v2_sle_mixeddata.py ${CODE}4.conf > ${CODE}4.results
python ../sequence-labeler-master/v2_sle_mixeddata.py ${CODE}5.conf > ${CODE}5.results
python ../sequence-labeler-master/v2_sle_mixeddata.py ${CODE}6.conf > ${CODE}6.results
python ../sequence-labeler-master/v2_sle_mixeddata.py ${CODE}7.conf > ${CODE}7.results
#python ../sequence-labeler-master/v2_sle_mixeddata.py ${CODE}8.conf > ${CODE}8.results
#python ../sequence-labeler-master/v2_sle_mixeddata.py ${CODE}9.conf > ${CODE}9.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}0.conf > ${CODE}0.results
python ../sequence-labeler-master/sequence_labeling_experiment.py ${CODE}0a.conf > ${CODE}0a.results

