#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    n = len(ar)
    max = 0
    for i in range(0, n):
        if(max < ar[i]):
            max = ar[i]

    max_counter = 0
    for i in range(0, n):
        if(ar[i] == max):
            max_counter += 1

    return max_counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
