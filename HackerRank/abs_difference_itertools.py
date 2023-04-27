#!/bin/python3
import itertools
import math
import os
import random
import re
import sys
from itertools import pairwise


#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    sorted_list = sorted(arr)
    # iter = pairwise(sorted_list)
    # min_difference = math.inf
    # for first, second in iter:
    #     if abs(first - second) < min_difference:
    #         min_difference = abs(first - second)
    # return min_difference
    min_difference = math.inf
    for i in range(1,len(sorted_list)):
        abs_difference = abs(sorted_list[i] - sorted_list[i-1])
        if abs_difference < min_difference:
            min_difference = abs_difference
    print(min_difference)






if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)
