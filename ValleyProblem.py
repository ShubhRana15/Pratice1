#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    i = 0
    count_valley = 0
    count_u = 0
    count_d = 0
    diff = [0] * n
    for c in s:
        if (c == 'U'):
            count_u += 1
        else:
            count_d += 1
        diff[i] = count_u - count_d
        i += 1
    for i in range(len(diff)):
        if (diff[i] == 0):
            if (s[i] == 'U'):
                count_valley += 1
    return (count_valley)


if __name__ == '__main__':

    result = countingValleys(16,"UDDDUUDDUUDUUDDU")

    print(str(result) + '\n')
