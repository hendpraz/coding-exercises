# Enter your code here. Read input from STDIN. Print output to STDOUT
k = 0
m = 0

def dive(row, curr_smax, arr):
    global k
    global m

    n = len(arr[row])
    if(row == k - 1):
        last_smax = 0
        for j in range(0, n):
            last_smax = max(last_smax, (curr_smax + (arr[row][j] ** 2)) % m)
        return last_smax
    else:    
        smax = 0
        for j in range(0, n):
            smax = max(smax, dive(row + 1, curr_smax + arr[row][j] ** 2, arr))
        return smax

def maximize_it():
    global k
    global m
    inp = input().split(' ')
    k = int(inp[0])
    m = int(inp[1])
    n = []
    arr = []
    smax = 0
    for i in range(0, k):
        arr.append(input().split(' '))
        n.append(int(arr[i][0]))
        arr[i].pop(0)

    for i in range(0, k):
        arr_len = len(arr[i])
        for j in range(0, arr_len):
            arr[i][j] = int(arr[i][j])

    if(k == 1):
        for j in range(0, n[0]):
            smax = max(smax, (arr[0][j] ** 2) % m)
    else:
        for j in range(0, n[0]):
            smax = max(smax, dive(1, arr[0][j] ** 2, arr))

    print(smax)
    
maximize_it()
