#!/bin/bash

export CODE='lc1-tol1-mix'
export THEANO_FLAGS='device=gpu1,floatX=float32'
python ../sequence-labeler-master/v2_sle_mixeddata.py ${CODE}6.conf > ${CODE}6.results
python ../sequence-labeler-master/v2_sle_mixeddata.py ${CODE}7.conf > ${CODE}7.results
python ../sequence-labeler-master/v2_sle_mixeddata.py ${CODE}8.conf > ${CODE}8.results
python ../sequence-labeler-master/v2_sle_mixeddata.py ${CODE}9.conf > ${CODE}9.results
