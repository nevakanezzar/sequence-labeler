#!/bin/bash

THEANO_FLAGS="device=gpu0,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py e51.conf > e51.results

THEANO_FLAGS="device=gpu0,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py e52.conf > e52.results

THEANO_FLAGS="device=gpu0,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py e53.conf > e53.results

THEANO_FLAGS="device=gpu0,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py e54.conf > e54.results

THEANO_FLAGS="device=gpu0,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py e55.conf > e55.results

THEANO_FLAGS="device=gpu0,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py e61.conf > e61.results

THEANO_FLAGS="device=gpu0,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py e62.conf > e62.results

THEANO_FLAGS="device=gpu0,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py e63.conf > e63.results

THEANO_FLAGS="device=gpu0,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py e64.conf > e64.results

THEANO_FLAGS="device=gpu0,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py e65.conf > e65.results

