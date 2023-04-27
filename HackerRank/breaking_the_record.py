#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    max = scores[0]
    min = scores[0]
    best = 0
    worst = 0
    for score in scores:
        if score > max:
            max = score
            best += 1
        if score < min:
            min = score
            worst += 1
    print([best,worst])

if __name__ == '__main__':

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
