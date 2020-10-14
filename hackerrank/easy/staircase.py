#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(0, n):
        start = n - 1
        stop = 0
        step = -1

        stop += step
        str_to_print = ""
        for j in range(start, stop, step):
            if(i >= j):
                str_to_print += '#'
            else:
                str_to_print += ' '
        
        print(str_to_print)

if __name__ == '__main__':
    n = int(input())

    staircase(n)
