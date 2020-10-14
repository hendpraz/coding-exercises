#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive_counter = 0
    zero_counter = 0
    negative_counter = 0
    arr_len = len(arr)
    
    for i in range(0, arr_len):
        if(arr[i] == 0):
            zero_counter += 1
        elif(arr[i] >= 1):
            positive_counter += 1
        else:
            negative_counter += 1

    print(float(positive_counter) / arr_len)
    print(float(negative_counter) / arr_len)
    print(float(zero_counter) / arr_len)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
