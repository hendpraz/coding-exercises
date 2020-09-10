# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(0, T):
    s = input()
    s_len = len(s)
    s_even = ''
    s_odd = ''
    for j in range (0, s_len):
        if(j % 2 == 0):
            s_even += s[j]
        else:
            s_odd += s[j]

    print(s_even + ' ' + s_odd)
