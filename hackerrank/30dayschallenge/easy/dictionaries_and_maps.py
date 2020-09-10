# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
phone_dict = {}
for i in range(0, n):
    inp = input().split(" ")
    phone_dict[inp[0]] = inp[1]

try:
    while(True):
        s = input()
        if(s in phone_dict):
            print(s + "=" + phone_dict[s])
        else:
            print('Not found')
except:
    exit()
