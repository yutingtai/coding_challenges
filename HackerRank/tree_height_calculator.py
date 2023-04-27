#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    length = 0
    for i in range(n+1):
        if i % 2 == 0:
            length += 1
        else:
            length *= 2
    return length


if __name__ == '__main__':
    n = 4
    print(utopianTree(n))
