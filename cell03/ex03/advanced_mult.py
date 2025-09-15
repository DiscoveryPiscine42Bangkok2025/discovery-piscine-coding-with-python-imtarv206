#!/usr/bin/env python3
import sys
if len(sys.argv) > 1:
    print(None)
    sys.exit(0)
i = 0
while i<=10:
    print(f"Table de {i}:", end=" ")
    j=0
    while j<=10:
        print(j*i, end=" ")
        j+=1
    print()
    i+=1