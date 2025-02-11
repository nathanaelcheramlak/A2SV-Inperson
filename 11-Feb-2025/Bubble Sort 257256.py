# Problem: Bubble Sort - https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    n = len(a)
    swap_count = 0
    for i in range(n):
        for j in range(n-i-1):
            if (a[j] > a[j + 1]):
                swap_count += 1
                a[j], a[j + 1] = a[j + 1], a[j]
    print(f"Array is sorted in {swap_count} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
