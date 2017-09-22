#!/bin/bash

THEANO_FLAGS="device=gpu1,floatX=float32" python ../sequence-labeler-master/sequence_labeling_experiment.py e2.3.small.conf > e2.3.small.results

THEANO_FLAGS="device=gpu1,floatX=float32" python ../sequence-labeler-master/sequence_labeling_experiment.py e1.3.small.conf > e1.3.small.results
