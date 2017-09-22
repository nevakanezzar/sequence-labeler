#!/bin/bash

THEANO_FLAGS="device=gpu0,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py e71.conf > e71.results

THEANO_FLAGS="device=gpu0,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py e72.conf > e72.results

THEANO_FLAGS="device=gpu0,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py e73.conf > e73.results

THEANO_FLAGS="device=gpu0,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py e74.conf > e74.results

THEANO_FLAGS="device=gpu0,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py e75.conf > e75.results

THEANO_FLAGS="device=gpu0,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py e76.conf > e76.results

THEANO_FLAGS="device=gpu0,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py e77.conf > e77.results

THEANO_FLAGS="device=gpu0,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py e78.conf > e78.results

THEANO_FLAGS="device=gpu0,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py e79.conf > e79.results
