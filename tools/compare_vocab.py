#!/bin/python3

import os
import sys

F1 = sys.argv[1]
F2 = sys.argv[2]

with open(F1,'r') as f:
    data = f.read().split()

v1 = set(data)

with open(F2,'r') as f:
    data = f.read().split()

v2 = set(data)

print("Length v1:",len(v1))
print("\n\n\nLength v2:",len(v2))
input()
print("\n\n\nv1 or v2:", len(v1|v2))
print("\n\n\nv1 and v2:", len(v1&v2))
input()
print("\n\n\nv1 less v2:", len(v1-v2))
print("\n\n\nv2 less v1:", len(v2-v1))

