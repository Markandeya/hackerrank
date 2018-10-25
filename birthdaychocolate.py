import math
import os
import random
import re
import sys


# s: an array of integers, the numbers on each of the squares of chocolate
# d: an integer, Ron's birth day
# m: an integer, Ron's birth month



# Complete the birthday function below.
def birthday(s, d, m):
    ways = 0
    cur = 0
    #1 2 1 3 2
    #3 2

    #m times loop
    for i in range(0, len(s)-m+1):
        tot = 0

        for j in range(i, i+m):
            tot += s[j]
        if tot == d:
            ways += 1
    
    return ways

if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    print(str(result) + '\n')
