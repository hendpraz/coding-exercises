# Enter your code here. Read input from STDIN. Print output to STDOUT

inp = input().split(' ')
actual_date = int(inp[0])
actual_month = int(inp[1])
actual_year = int(inp[2])

inp = input().split(' ')
expected_date = int(inp[0])
expected_month = int(inp[1])
expected_year = int(inp[2])

if(actual_year > expected_year):
    print(10000)
else:
    if(actual_year == expected_year):
        if(actual_month > expected_month):
            print(500 * abs(expected_month - actual_month))
        else:
            if(actual_month == expected_month):
                print(15 * abs(expected_date - actual_date))
            else:
                print(0)
    else:
        print(0)
