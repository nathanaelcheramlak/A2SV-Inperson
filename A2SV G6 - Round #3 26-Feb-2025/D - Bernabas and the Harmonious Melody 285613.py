# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D

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

def solve(melodies, n):
    melody_set = set(melodies)
    minimum_removal = float('inf')
    for melody in melody_set:
        minimum = count_removal(melodies, melody)
        if minimum != -1:
            minimum_removal = min(minimum_removal, minimum)

    if minimum_removal == float('inf'):
        return -1
    return minimum_removal

def count_removal(melodies, melody): # (melody) to be removed
    left = 0
    right = len(melodies) - 1
    count = 0
    
    while right > left:
        if melodies[right] == melodies[left]:
            left += 1
            right -= 1
        elif melodies[left] == melody:
            left += 1
            count += 1
        elif melodies[right] == melody:
            right -= 1
            count += 1
        else:
            return -1
        
    return count

if __name__ == '__main__':
    for _ in range(iinput()):
        # Receive input
        n = iinput()
        melodies = list(map(str, input().strip()))

        ans = solve(melodies, n)
        print(ans)