#!/bin/bash

THEANO_FLAGS="device=gpu0,floatX=float32" python ../sequence-labeler-master/sequence_labeling_experiment.py e0.conf > e0.results

THEANO_FLAGS="device=gpu0,floatX=float32" python ../sequence-labeler-master/sequence_labeling_experiment.py e1.1.conf > e1.1.results

THEANO_FLAGS="device=gpu0,floatX=float32" python ../sequence-labeler-master/sequence_labeling_experiment.py e1.2.conf > e1.2.results

THEANO_FLAGS="device=gpu0,floatX=float32" python ../sequence-labeler-master/sequence_labeling_experiment.py e1.4.conf > e1.4.results

THEANO_FLAGS="device=gpu0,floatX=float32" python ../sequence-labeler-master/sequence_labeling_experiment.py e2.1.conf > e2.1.results

THEANO_FLAGS="device=gpu0,floatX=float32" python ../sequence-labeler-master/sequence_labeling_experiment.py e2.2.conf > e2.2.results

THEANO_FLAGS="device=gpu0,floatX=float32" python ../sequence-labeler-master/sequence_labeling_experiment.py e2.4.conf > e2.4.results

THEANO_FLAGS="device=gpu0,floatX=float32" python ../sequence-labeler-master/sequence_labeling_experiment.py e2.3.conf > e2.3.results

THEANO_FLAGS="device=gpu0,floatX=float32" python ../sequence-labeler-master/sequence_labeling_experiment.py e1.3.conf > e1.3.results
