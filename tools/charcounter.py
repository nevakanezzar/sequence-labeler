import os
import sys

trigram_set = set()

IN_FILE = sys.argv[1] #if error, please give input filename.

with open(IN_FILE) as f:
    a = f.read(1)
    b = f.read(1)
    while True:
        c = f.read(1)
        if not c:
            print("End of file")
            break
        
        trigram_set.add(a+b+c)
        a = b
        b = c

print(len(trigram_set))

