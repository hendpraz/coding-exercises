# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())
for i in range(0, T):
    try:
        inp = input().split(" ")
        a = int(inp[0])
        b = int(inp[1])
        print(a//b)
    except BaseException as e:
        print ("Error Code:",e)
