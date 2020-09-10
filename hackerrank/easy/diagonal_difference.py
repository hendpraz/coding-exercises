#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    primary_diagonal = 0
    secondary_diagonal = 0
    
    i = 0
    while(i < n):
        primary_diagonal += arr[i][i]
        i += 1
    
    i = 0
    j = n - 1
    while(i < n) and (j >= 0):
        secondary_diagonal += arr[i][j]
        i += 1
        j -= 1

    return abs(primary_diagonal - secondary_diagonal)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
