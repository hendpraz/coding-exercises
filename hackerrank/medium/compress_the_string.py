# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()
s_len = len(s)
num = ''
occurs = 0
for i in range(s_len):
    if(s[i] == num):
        occurs += 1
    else:
        if (num != ''):
            print((occurs, int(num)), end=' ')
        num = s[i]
        occurs = 1
print((occurs, int(num)))