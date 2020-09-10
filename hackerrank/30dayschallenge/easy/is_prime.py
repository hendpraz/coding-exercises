# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def isPrime(n):
    sq_n = int(math.sqrt(n)) + 1
    prime = True
    if(n == 1):
        prime = False
    else:
        for i in range(2, sq_n):
            if(n % i == 0):
                prime = False
                break
                
    if(prime):
        print("Prime")
    else:
        print("Not prime")



T = int(input())
for i in range(T):
    n = int(input())
    isPrime(n)
