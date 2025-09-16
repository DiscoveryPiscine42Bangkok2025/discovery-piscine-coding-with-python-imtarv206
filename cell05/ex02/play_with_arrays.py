#!/usr/bin/env python3
arr = [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = []
for a in arr:
    if a>5:
        new_arr.append(a+2)

print(f"{arr}")
print(f"{new_arr}")