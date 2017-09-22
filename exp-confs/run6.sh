#!/bin/bash

THEANO_FLAGS="device=gpu1,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py e66.conf > e66.results

THEANO_FLAGS="device=gpu1,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py e67.conf > e67.results

THEANO_FLAGS="device=gpu1,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py e68.conf > e68.results

THEANO_FLAGS="device=gpu1,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py e69.conf > e69.results

