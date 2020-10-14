#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valley = 0
    level = 0
    is_in_valley = False
    for i in range (0, n):
        if(s[i] == 'U'):
            level = level + 1
        else: #s[i] == D
            level = level - 1

        if(is_in_valley) and (level == 0):
            valley += 1
            is_in_valley = False

        if(level < 0) and (not(is_in_valley)):
            is_in_valley = True

    return valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
