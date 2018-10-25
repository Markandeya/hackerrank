# Complete the function gradingStudents in the editor below.
# It should return an integer array consisting of rounded grades. 
# Round to nearest multiple of 5 if difference is less than 3
# and total not less than 38

import os
import sys
import math

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    newmarks = []
    for mark in grades:
        if mark <38:
            newmarks.append(mark)
        else:
            q = mark/5
            m = math.ceil(q)*5
            print("m = {}".format(m))
            diff = m - mark
            print("diff = {}".format(diff))
            if diff<3:
                newmarks.append(m)
            else:
                newmarks.append(mark)

    return newmarks

if __name__ == '__main__':

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print('\n'.join(map(str, result)))
    print('\n')