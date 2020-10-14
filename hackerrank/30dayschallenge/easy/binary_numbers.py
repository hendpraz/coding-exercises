#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    max_streak = 0
    streak = 0
    while(n > 0):
        if(n % 2 == 1):
            streak += 1
            if(streak > max_streak):
                max_streak = streak
        else:
            streak = 0
        n = int(n / 2)
    print(max_streak)
