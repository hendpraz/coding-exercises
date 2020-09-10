#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s_len = len(s)
    matrix = []
    sqroot = math.sqrt(s_len)
    if(sqroot - int(sqroot) < 0.0000001):
        row = int(sqroot)
        col = row
    else:
        row = int(sqroot)
        col = row + 1
        if((row * col) < s_len):
            row += 1 

    print(str(row) + ' ' + str(col))
    for i in range (0, row):
        arr = []
        for j in range (0, col):
            idx = i * col + j
            if(idx < s_len):
                arr.append(s[idx])
            else:
                arr.append('#')
        matrix.append(arr)

    print(matrix)
    str_to_print = ''
    for i in range(0, col):
        for j in range (0, row):
            temp = matrix[j][i]
            if(temp == '#'):
                str_to_print += ''
            else:
                str_to_print += temp
        str_to_print += ' '

    return str_to_print

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
