import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if (x1>=x2 and v1>v2) or (x2>=x1 and v2>v1):
        return 'NO'

    if x1>x2 and v1 != v2:
        diff = x1 - x2
        if diff%(v2-v1) == 0:
            return 'YES'
        else:
            return 'NO'
    elif x2>x1 and v1 != v2:
        diff = x2 - x1
        if diff%(v1-v2) == 0:
            return 'YES'
        else:
            return 'NO'
    elif (x1>x2 or x2>x1) and v1 == v2:
        return 'NO'
    else:
        if v1 == v2:
            return 'YES'
        else:
            return 'NO'


if __name__ == '__main__':

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result + '\n')