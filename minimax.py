import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(ar):
    for i in range(0, len(ar) - 1 ):
        max = ar[0]
        pos = 0
        for j in range(0, len(ar) - i):
            if ar[j] > max:
                max = ar[j]
                pos = j
        ar[pos] = ar[j]
        ar[j] = max
    min, max = 0, 0
    
    for i in range(0,len(ar)-1):
        min += ar[i]
    for i in range(len(ar)-1, 0, -1):
        max += ar[i]
    print('{} {}'.format(min,max))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
