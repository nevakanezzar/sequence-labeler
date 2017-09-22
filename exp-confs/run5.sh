#!/bin/bash

THEANO_FLAGS="device=gpu1,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py e56.conf > e56.results

THEANO_FLAGS="device=gpu1,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py e57.conf > e57.results

THEANO_FLAGS="device=gpu1,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py e58.conf > e58.results

THEANO_FLAGS="device=gpu1,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py e59.conf > e59.results

THEANO_FLAGS="device=gpu1,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py a6.conf > a6.results

THEANO_FLAGS="device=gpu1,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py a7.conf > a7.results

THEANO_FLAGS="device=gpu1,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py a8.conf > a8.results

THEANO_FLAGS="device=gpu1,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py a9.conf > a9.results

THEANO_FLAGS="device=gpu1,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py b6.conf > b6.results

THEANO_FLAGS="device=gpu1,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py b7.conf > b7.results

THEANO_FLAGS="device=gpu1,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py b8.conf > b8.results

THEANO_FLAGS="device=gpu1,floatX=float32" python ../sequence-labeler-master/v2_sle_mixeddata.py b9.conf > b9.results

