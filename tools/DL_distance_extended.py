import sys
import os
import numpy as np

def ins_cost(a):
    return 1

def del_cost(a):
    return 1

def sub_cost(a,b):
    if a.lower() == b.lower():
        return 0
    else:
        return min(DL_distance_extended(a.split(""),b.split(""))/(len(a)+len(b)),1.99999)

def trans_cost(a,b):
    return len(a)-1

def DL_distance_extended(a, b):
    d = np.zeros([len(a), len(b)])
    for i in range(0, len(a)+1):
        d[i, 0] = i
    for j in range(0, len(b)+1):
        d[0, j] = j

    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i] == b[j]:
                d[i,j] = 0
            else:
                d[i,j] = min(d[i-1,j  ] + del_cost(a[i]),
                             d[i  ,j-1] + ins_cost(b[j]),
                             d[i-1,j-1] + sub_cost(a[i],b[j]))

            # Damerau-Levenshtein extension for multi-token transpositions
            k = 1
            while i > 1 and j > 1 and (i - k) >= 1 and (j - k) >= 1 and d[i-k, j-k] - d[i-k-1, j-k-1] > 0:
                if sorted(a[i-k:i+1].lower()) == sorted(b[j-k:j+1].lower()):
                    d[i, j] = min(d[i, j], d[i-k, j-k] + trans_cost(a[i-k:i+1], b[j-k:j+1]))
                    break
                k += 1



    return d[len(a), len(b)]


