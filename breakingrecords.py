import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    count = [0,0]
    min = max = scores[0]

    for i in range(1, len(scores)):
        if scores[i] < min:
            min = scores[i]
            count[1] += 1
        elif scores[i] > max:
            max = scores[i]
            count[0] += 1

    return count


if __name__ == '__main__':

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(' '.join(map(str, result)))
    print('\n')
