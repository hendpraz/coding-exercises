# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

N = int(input())
inp = input().split(' ')
K = int(input())

nums = [n for n in range(0, N)]
combins = list(combinations(nums, K))

count_a = 0
a_idx = []
for i in range(len(inp)):
    if(inp[i] == 'a'):
        a_idx.append(i)

for i in range(len(combins)):
    found = False
    for j in range(len(a_idx)):
        if(found):
            continue
        if(a_idx[j] in combins[i]):
            count_a += 1
            found = True
        

print(count_a / len(combins))
