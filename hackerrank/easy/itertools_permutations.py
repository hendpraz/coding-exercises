# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

inp = (input()).split()

list_permutations = list(permutations(inp[0], int(inp[1])))

output_list =[]
for tuple in list_permutations:
    output_list.append(''.join(tuple))

output_list = sorted(output_list)
for s in output_list:
    print(s)
