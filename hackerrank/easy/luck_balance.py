#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    contests = sorted(contests, reverse=True)
    
    total = 0
    for i in range(len(contests)):
        if(contests[i][1] == 1):
            if(k > 0):
                total += contests[i][0]
                k -= 1
            else:
                total -= contests[i][0]
        else:
            total += contests[i][0]

    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
