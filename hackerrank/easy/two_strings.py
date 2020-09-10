#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    mydict = dict()
    for char in s1:
        mydict[char] = True

    share = False
    for char in s2:
        if(char in mydict):
            share = True
            break

    if(share):
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
