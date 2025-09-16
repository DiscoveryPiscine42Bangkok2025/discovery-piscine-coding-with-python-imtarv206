#!/usr/bin/env python3
import sys
if len(sys.argv) >= 3:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    ans = []
    for i in range(start,end+1):
        ans.append(i)
    print(ans)
else:
    print("none")