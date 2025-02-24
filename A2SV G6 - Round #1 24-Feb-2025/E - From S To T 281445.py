# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

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

def solve(s, t, p):
    # Check if s is a sub-sequence of t
    pt = 0
    for letter in s:
        while pt < len(t) and t[pt] != letter:
            pt += 1
        if pt >= len(t) or t[pt] != letter:
            return False
        else:
            pt += 1
    
    bank = Counter(s + p)
    
    for letter in t:
        if letter in bank:
            bank[letter] -= 1
        else:
            return False
        
        if bank[letter] == 0:
            del bank[letter]
    
    return True


if __name__ == '__main__':
    for _ in range(iinput()):
        # Receive input
        s = list(input().strip())
        t = list(input().strip())
        p = list(input().strip())

        ans = solve(s, t, p)
        if ans:
            print("YES")
        else:
            print("NO")