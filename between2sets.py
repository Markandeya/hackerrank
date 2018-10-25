import os
import sys
from functools import reduce

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    mini = reduce(lcm, a)
    maxi = reduce(gcd, b) 
    c = 0
    for i in range(mini, maxi+1, mini):
        if maxi%i==0: c += 1

    return c

def gcd(a, b):
    while b!=0:
         a, b = b, a%b
    return a

def lcm(a, b):
    return a*b//gcd(a, b)

if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    print(str(total) + '\n')