# Problem: Counting Sort  - https://www.hackerrank.com/challenges/countingsort1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def countingSort(arr):
    bucket = [0] * 100
    
    for num in arr:
        bucket[num] += 1
        
    return bucket
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
