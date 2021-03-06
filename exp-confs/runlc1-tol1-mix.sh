#!/bin/bash

export CODE='lc1-tol1-mix'
export THEANO_FLAGS='device=gpu2,floatX=float32'
python ../sequence-labeler-master/v2_sle_mixeddata.py ${CODE}1.conf > ${CODE}1.results
python ../sequence-labeler-master/v2_sle_mixeddata.py ${CODE}2.conf > ${CODE}2.results
python ../sequence-labeler-master/v2_sle_mixeddata.py ${CODE}3.conf > ${CODE}3.results
python ../sequence-labeler-master/v2_sle_mixeddata.py ${CODE}4.conf > ${CODE}4.results
