#!/bin/bash

THEANO_FLAGS="device=gpu0,floatX=float32" python ../sequence-labeler-master/sequence_labeling_experiment.py e3.conf > e3.results

