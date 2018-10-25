'''
Program to find how many apples and oranges fell in Sam's house
given that on a number line-
s,t is start-end of house
a,b is position of apple and orange tree respectively
apples, oranges are the distances at which they fall eg: [1,-2] 

'''
import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    house = range(s,t+1)
    na, no = 0, 0

    for i in range(0, len(apples)):
        apples[i] += a
        if apples[i] in house:
            na += 1
    for i in range(0, len(oranges)):
        oranges[i] += b
        if oranges[i] in house:
            no += 1
    print("{}\n{}".format(na, no))


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
