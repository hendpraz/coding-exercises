#!/bin/python3

import sys

S = input().strip()
try:
    val = int(S)
    print(val)
except ValueError:
    print("Bad String")