#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    required = {}
    for i in range(len(cost)):
        if money - cost[i] in required:
            temp = [required[money - cost[i]],i]
            break
        else:
            required[cost[i]] = i

    for i in temp:
        print(i + 1 ,end=' ')
    print()

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
