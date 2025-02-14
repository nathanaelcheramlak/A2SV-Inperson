# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

from collections import Counter, defaultdict, deque
from math import ceil, floor, gcd, inf, log2, sqrt
from cmath import inf


def iinput(): return int(input())
def sinput(): return input()
def iarray(): return list(map(int, input().split()))
def imatrix(rows): return [list(map(int,input().split())) for _ in range(rows)]
def smatrix(rows): return [input() for _ in range(rows)]
def mapint(): return map(int, input().split())

# _   _  ____ 
# | \ | |/ ___|
# |  \| | | 
# | |\  | |___ 
# |_| \_|\____|

def solve(nums, n):
    prev = nums[0]
    total_sum = nums[0]

    for i in range(1, n):
        if prev < 0:
            if nums[i] < 0 and nums[i] > prev:
                total_sum -= prev
                total_sum += nums[i]
                prev = nums[i]
            elif nums[i] > 0:
                total_sum += nums[i]
                prev = nums[i]
        else:
            if nums[i] > 0 and nums[i] > prev:
                total_sum -= prev
                total_sum += nums[i]
                prev = nums[i]
            elif nums[i] < 0:
                total_sum += nums[i]
                prev = nums[i]
    
    return total_sum

if __name__ == '__main__':
    t = iinput()
    for _ in range(t):
        # Receive input
        n = iinput()
        nums = iarray()
        ans = solve(nums, n)
        print(ans)
