#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    mydict = dict()
    for word in magazine:
        mydict[word] = 0
    
    for word in magazine:
        mydict[word] += 1
    
    yes = True
    for word in note:
        if(word not in mydict):
            yes = False
            break
        else:
            if(mydict[word] == 0):
                yes = False
                break
            else:
                mydict[word] -= 1

    if(yes):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
