#!/usr/bin/env python3
usr_input = input("")
# ans = usr_input.swapcase()
# print(ans)

result = ""
for ch in usr_input:
    if ch.isupper():
        result += ch.lower()
    elif ch.islower():
        result += ch.upper()
    else:
        result += ch
print(result)