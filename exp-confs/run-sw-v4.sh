#!/bin/bash


export CODE='sw-v4-0a'
export THEANO_FLAGS='device=gpu1,floatX=float32'
python ../sequence-labeler-master/v4_sle_sizeoffirst.py ${CODE}1.conf > ${CODE}1.results
python ../sequence-labeler-master/v4_sle_sizeoffirst.py ${CODE}2.conf > ${CODE}2.results
python ../sequence-labeler-master/v4_sle_sizeoffirst.py ${CODE}3.conf > ${CODE}3.results
python ../sequence-labeler-master/v4_sle_sizeoffirst.py ${CODE}4.conf > ${CODE}4.results
python ../sequence-labeler-master/v4_sle_sizeoffirst.py ${CODE}5.conf > ${CODE}5.results
python ../sequence-labeler-master/v4_sle_sizeoffirst.py ${CODE}6.conf > ${CODE}6.results
python ../sequence-labeler-master/v4_sle_sizeoffirst.py ${CODE}7.conf > ${CODE}7.results
python ../sequence-labeler-master/v4_sle_sizeoffirst.py ${CODE}8.conf > ${CODE}8.results
python ../sequence-labeler-master/v4_sle_sizeoffirst.py ${CODE}9.conf > ${CODE}9.results
python ../sequence-labeler-master/v4_sle_sizeoffirst.py ${CODE}10.conf > ${CODE}10.results
