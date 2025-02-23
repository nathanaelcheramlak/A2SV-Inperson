# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

from collections import Counter, defaultdict, deque
from math import ceil, floor, gcd, inf, log2, sqrt
from cmath import inf


def iinput(): return int(input())
def sinput(): return input()
def iarray(): return list(map(int, input().split()))
def imatrix(rows): return [list(map(int,input().split())) for _ in range(rows)]
def smatrix(rows): return [input() for _ in range(rows)]
def mapint(): return map(int, input().split())

#  _   _  ____ 
# | \ | |/ ___|
# |  \| | | 
# | |\  | |___ 
# |_| \_|\____|

def solve(a, b, n, m):
    one = 0
    two = 0
    count = 0

    sum_a = 0
    sum_b = 0

    while one < n and two < m:
        sum_a += a[one]
        sum_b += b[two]
        if sum_a == sum_b:
            count += 1
            sum_a = 0
            sum_b = 0
            one += 1
            two += 1
        elif sum_b > sum_a:
            one += 1
            sum_b -= b[two]
        else:
            two += 1
            sum_a -= a[one]

    if one != n or two != m:
        return -1
    return count
    

if __name__ == '__main__':
    n = iinput()
    a = iarray()
    m = iinput()
    b = iarray()
    
    ans = solve(a, b, n, m)
    print(ans)