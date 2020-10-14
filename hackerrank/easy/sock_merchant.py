#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar_counter = []
    for i in range(0, 101):
        ar_counter.append(0)

    for i in range(0, n):
        ar_counter[ar[i]] += 1

    total_pair = 0
    for i in range(0, 101):
        pair_count = int(ar_counter[i] / 2)
        total_pair += pair_count
    return total_pair


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
