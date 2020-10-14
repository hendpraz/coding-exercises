#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    max_sum = -9 * 7
    for i in range(4):
        for j in range(4):
            sum_hourglass = 0
            for k in range(3):
                for l in range(3):
                    if(k == 1) and (l != 1):
                        continue
                    else:
                        sum_hourglass += arr[i+k][j+l]
            if(max_sum < sum_hourglass):
                max_sum = sum_hourglass

    print(max_sum)