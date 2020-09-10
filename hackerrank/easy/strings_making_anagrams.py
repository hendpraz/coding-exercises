#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    dict_a = dict()
    dict_b = dict()

    for i in range(len(a)):
        if(a[i] in dict_a):
            dict_a[a[i]] += 1
        else:
            dict_a[a[i]] = 1
    
    for i in range(len(b)):
        if(b[i] in dict_b):
            dict_b[b[i]] += 1
        else:
            dict_b[b[i]] = 1
    
    total = 0
    for x in dict_a:
        if(x in dict_b):
            if(dict_a[x] > dict_b[x]):
                total += (dict_a[x] - dict_b[x])
                dict_a[x] = dict_b[x]
            elif(dict_a[x] < dict_b[x]):
                total += (dict_b[x] - dict_a[x])
                dict_b[x] = dict_a[x]
        else:
            total += dict_a[x]
            dict_a[x] = 0

    for x in dict_b:
        if(x not in dict_a):
            total += dict_b[x]
            dict_b[x] = 0

    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
