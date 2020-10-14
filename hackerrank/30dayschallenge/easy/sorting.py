#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

numSwaps = 0

for i in range(0, len(a)):
    numberOfSwaps = 0
    for j in range(0, len(a) - 1):
        if (a[j] > a[j + 1]):
            # swap(a[j], a[j + 1])
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp
            numberOfSwaps += 1
            numSwaps +=1

    if(numberOfSwaps == 0):
        break        

print('Array is sorted in ' + str(numSwaps) + ' swaps.')
print('First Element: ' + str(a[0]))
print('Last Element: ' + str(a[len(a) - 1]))
