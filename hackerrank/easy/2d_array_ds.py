#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    size = len(arr)
    max_arr = -999
    for i in range(0, size - 2):
        for j in range(0, size - 2):
            sum_arr = 0
            for k in range(0, 3):
                for l in range(0, 3):
                    if((k == 1) and ((l == 0) or (l == 2))):
                        continue
                    else:
                        sum_arr += arr[i+k][j+l]
            
            if(max_arr < sum_arr):
                max_arr = sum_arr

    return max_arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
