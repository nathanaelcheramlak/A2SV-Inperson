# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

from collections import Counter, defaultdict, deque
from math import ceil, floor, gcd, inf, log2, sqrt
from cmath import inf


def iinput(): return int(input())
def sinput(): return input()
def iprefixay(): return list(map(int, input().split()))
def imatrix(rows): return [list(map(int,input().split())) for _ in range(rows)]
def smatrix(rows): return [input() for _ in range(rows)]
def mapint(): return map(int, input().split())

#  _   _  ____ 
# | \ | |/ ___|
# |  \| | | 
# | |\  | |___ 
# |_| \_|\____|

def solve():
    pass

if __name__ == '__main__':
    # Receive input
    n, k, q = mapint()
    prefix = [0] * (200001)

    for _ in range(n):
        l, r = mapint()
        prefix[l] += 1
        if r < 200000:
            prefix[r + 1] -= 1
    
    # Calculate the prefix sum
    for i in range(1, 200001):
        prefix[i] += prefix[i - 1]
    
    # Convert to binary
    for i, pre in enumerate(prefix):
        if pre >= k:
            prefix[i] = 1
        else:
            prefix[i] = 0

    # Calculate the prefix sum again
    for i in range(1, 200001):
        prefix[i] += prefix[i - 1]

    for _ in range(q):
        l, r = mapint()
        ans = prefix[r]- prefix[l - 1]
        print(ans)

