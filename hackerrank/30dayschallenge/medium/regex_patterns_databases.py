#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    gmailUsers = []

    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        if(re.match("\S*@gmail.com", emailID)):
            gmailUsers.append(firstName)
    
    gmailUsers.sort()
    for i in range(len(gmailUsers)):
        print(gmailUsers[i])
