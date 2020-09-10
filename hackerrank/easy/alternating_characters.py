#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    s_list = []
    last = s[0]
    s_list.append(last)
    erase = 0

    for i in range(1, len(s)):
        if(last != s[i]):
            s_list.append(s[i])
            last = s[i]
        else:
            erase += 1

    return erase

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
