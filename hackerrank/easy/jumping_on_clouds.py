#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    n = len(c)

    if(n == 0):
        return 0
    elif(c[0] != 0):
        return 999
    else:
        temp1 = list(c)
        temp1.pop(0)
        if(len(temp1) >= 2):
            path1 = jumpingOnClouds(temp1)
            temp2 = list(temp1)
            temp2.pop(0)
            path2 = jumpingOnClouds(temp2)
        else:
            if(len(temp1) == 1):
                path1 = jumpingOnClouds(temp1)
            else:
                return 0
            path2 = 0
        return 1 + min(path1, path2)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
