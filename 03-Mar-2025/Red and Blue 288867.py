# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

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
    for _ in range(iinput()):
        # Receive input
        n = iinput()
        a = iarray()
        m = iinput()
        b = iarray()

        a_max = 0
        acc = 0
        for num in a:
            acc += num
            a_max = max(a_max, acc)

        b_max = 0
        acc = 0
        for num in b:
            acc += num
            b_max = max(b_max, acc)

        print(a_max + b_max)
