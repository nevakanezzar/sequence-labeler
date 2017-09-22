#!/bin/bash

THEANO_FLAGS="device=gpu1,floatX=float32" python ../sequence-labeler-master/sequence_labeling_experiment.py e2.3.large.conf > e2.3.large.results

THEANO_FLAGS="device=gpu1,floatX=float32" python ../sequence-labeler-master/sequence_labeling_experiment.py e1.3.large.conf > e1.3.large.results
