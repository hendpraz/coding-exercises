#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    for i in range(1, 11):
        str_to_print = str(n) + ' x ' + str(i) + ' = ' + str(i * n)
        print(str_to_print)
