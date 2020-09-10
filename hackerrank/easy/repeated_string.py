#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    total = 0
    a_counter = s.count('a')
    s_len = len(s)
    
    a_counter *= int(n / s_len)
    remainder = n % s_len
    for i in range(0, remainder):
        if(s[i] == 'a'):
            a_counter += 1

    return a_counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
