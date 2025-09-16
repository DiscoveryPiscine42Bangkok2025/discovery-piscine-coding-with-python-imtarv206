#!/usr/bin/env python3
import sys
if len(sys.argv) > 1:
    usr_input = input("What was the parameter? ")
    if sys.argv[1] == usr_input:
        print("Good job!")
    else:
        print("Nope, sorry...")
    
else:
    print("none")