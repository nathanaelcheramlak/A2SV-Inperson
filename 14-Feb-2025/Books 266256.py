# Problem: Books - https://codeforces.com/contest/279/problem/B

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

def solve(books, n, t):
    count = 0
    time = 0
    left = 0

    for right in range(n):
        time += books[right]
        while time > t:
            time -= books[left]
            left += 1
        count = max(count, right - left + 1)
    
    return count



if __name__ == '__main__':
    # Receive input
    n, t = mapint()
    books = iarray()

    ans = solve(books, n, t)
    print(ans)
    # if ans:
    #     print("YES")
    # else:
    #     print("NO")
