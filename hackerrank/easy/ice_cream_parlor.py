#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    new_arr = sorted(arr)
    i = 0
    j = len(arr) - 1
    while i != j:
        if new_arr[i] + new_arr[j] == m:
            break
        elif new_arr[i] + new_arr[j] > m:
            j -= 1
        else:
            i += 1

    first_idx = arr.index(new_arr[i])
    second_idx = arr.index(new_arr[j])

    if first_idx == second_idx:
        arr.pop(first_idx)
        second_idx = arr.index(new_arr[j]) + 1
    elif first_idx > second_idx:
        temp = first_idx
        first_idx = second_idx
        second_idx = temp

    return ((first_idx + 1, second_idx + 1))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
