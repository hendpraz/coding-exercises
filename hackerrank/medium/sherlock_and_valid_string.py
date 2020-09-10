#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    mydict = dict()
    
    min_occurence = 10 ** 5
    for i in range(len(s)):
        if(s[i] in mydict):
            mydict[s[i]] += 1
        else:
            mydict[s[i]] = 1

    for val in mydict.values():
        if(val < min_occurence):
            min_occurence = val

    if(min_occurence == 1):
        not_min = min_occurence
        for key in mydict:
            if(mydict[key] != min_occurence):
                not_min = mydict[key]
                break

        remove = True
        chance = True
        for key in mydict:
            if(mydict[key] != not_min):
                if(chance):
                    chance = False
                else:
                    remove = False

        if(remove):
            return 'YES'
    
    chance = True
    for key in mydict:
        if(mydict[key] > min_occurence + 1):
            return 'NO'
        elif(mydict[key] == min_occurence + 1):
            if(chance):
                mydict[key] -= 1
                chance = False
            else:
                return 'NO'

    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
