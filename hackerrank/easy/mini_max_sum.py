#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum_arr = 0
    arr_len = len(arr)
    for i in range(0, arr_len):
        sum_arr += arr[i]

    max_sum = 0
    min_sum = 10 ** 10
    for i in range(0, arr_len):
        if(sum_arr - arr[i] > max_sum):
            max_sum = sum_arr - arr[i]
        
        if(sum_arr - arr[i] < min_sum):
            min_sum = sum_arr - arr[i]

    print(str(min_sum) + ' ' + str(max_sum))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
