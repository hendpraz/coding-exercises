#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    total = 0
    mydict = dict()
    for i in range(0, len(s)):
        mydict.clear()
        for j in range(0, len(s) - i):
            temp = s[j:j+i+1]
            temp = ''.join(sorted(temp))
            if temp in mydict:
                mydict[temp] += 1
            else:
                mydict[temp] = 1
        
        print(mydict)

        for val in mydict.values():
            if(val > 1):
                temp2 = 0
                for j in range(1, val):
                    temp2 += j
                total += temp2
                print(total)

    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
