#!/bin/bash

export CODE='t'
export THEANO_FLAGS='device=gpu2,floatX=float32'
python ../sequence-labeler-master/v3_sle_batchwisedata.py ${CODE}1.conf > ${CODE}1.results
python ../sequence-labeler-master/v3_sle_batchwisedata.py ${CODE}2.conf > ${CODE}2.results
python ../sequence-labeler-master/v3_sle_batchwisedata.py ${CODE}3.conf > ${CODE}3.results
python ../sequence-labeler-master/v3_sle_batchwisedata.py ${CODE}4.conf > ${CODE}4.results

export CODE='e'
python ../sequence-labeler-master/v2_sle_mixeddata.py ${CODE}9.conf > ${CODE}9.results


