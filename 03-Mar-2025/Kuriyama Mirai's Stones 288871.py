# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

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

def solve():
    pass

if __name__ == '__main__':
    n = iinput()
    arr = iarray()
    q = iinput()

    prefix = [0]
    acc = 0
    for num in arr:
        acc += num
        prefix.append(acc)
    
    arr.sort()
    sorted_prefix = [0]
    acc = 0
    for num in arr:
        acc += num
        sorted_prefix.append(acc)
    
    for _ in range(q):
        t, l, r = mapint()
        if t == 1:
            ans = prefix[r] - prefix[l - 1] 
            print(ans)
        else:
            ans = sorted_prefix[r] - sorted_prefix[l - 1]
            print(ans)