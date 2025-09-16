#!/usr/bin/env python3
import sys
import re

if len(sys.argv) != 2:
    print("none")
else:
    check_in = sys.argv[1]
    found = re.findall('z', check_in)
    if found:
        for chr in found:
            print(chr, end="")
        print()
    else:
        print("none")
