#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    arrlen = len(arr)
    pdiagsum, sdiagsum = 0, 0
    
    for i in range(0, arrlen):
        pdiagsum = pdiagsum + arr[i][i]
        sdiagsum = sdiagsum + arr[i][ arrlen -1 - i]
    return abs(pdiagsum - sdiagsum)
    

if __name__ == '__main__':

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
