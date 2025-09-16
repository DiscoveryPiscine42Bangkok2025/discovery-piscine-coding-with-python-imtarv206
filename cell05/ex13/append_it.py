#!/usr/bin/env python3
import sys
if len(sys.argv) < 2:
    print("none")
else:
    words = sys.argv[1:]
    for arg in words:
        if("ism" not in arg):
            print(arg+'ism')