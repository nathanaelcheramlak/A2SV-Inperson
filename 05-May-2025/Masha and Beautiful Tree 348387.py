# Problem: Masha and Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

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

def solve(arr, n):
    count = [0]
    def divide(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = divide(arr[:mid])
        right = divide(arr[mid:])

        return merge(left, right)
    def merge(left, right):
        if left[0] < right[0]:
            return left + right
        count[0] += 1
        return right + left

    s = divide(arr)
    if sorted(arr) != s:
        return -1
    return count[0]


if __name__ == '__main__':
    for _ in range(iinput()):
        n = iinput()
        arr = iarray()

        ans = solve(arr, n)
        print(ans)