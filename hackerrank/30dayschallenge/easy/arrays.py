#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    arr_len = len(arr)
    str_to_print = ''
    for i in range(arr_len - 1, 0, -1):
        str_to_print += str(arr[i]) + ' '
    str_to_print += str(arr[0])
    print(str_to_print)
