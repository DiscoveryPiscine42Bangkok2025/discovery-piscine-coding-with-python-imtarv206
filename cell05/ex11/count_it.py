#!/usr/bin/env python3
import sys
import re
if len(sys.argv) > 2:
    param = sys.argv[1:]
    print(f"parameters: {len(param)}")
    for arg in param:
        print(f"{arg}: {len(arg)}")
else:
    print("none")