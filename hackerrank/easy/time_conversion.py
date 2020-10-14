#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    string_to_print = (s[2:])[:6]
    temp = int(s[0] + s[1])
    
    if(s[8] == 'P'):
        temp = temp + 12
        if(temp == 24):
            temp = 12
    else:
        if(temp == 12):
            temp = 0

    string_to_print = str(int(temp / 10)) + str(temp % 10) + string_to_print

    return string_to_print

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
