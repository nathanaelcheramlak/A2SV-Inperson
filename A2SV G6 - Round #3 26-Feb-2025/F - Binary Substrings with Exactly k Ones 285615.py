# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

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

def solve(nums, k):
    running_dict = {0: 1}
    count = 0
    running_sum = 0
    for num in nums:
        running_sum += num
        if (running_sum - k) in running_dict:
            count += running_dict[running_sum - k]
        running_dict[running_sum] = running_dict.get(running_sum, 0) + 1

    return count 
    

if __name__ == '__main__':
    k = iinput()
    binary = list(map(int, input().strip()))
    
    ans = solve(binary, k)
    print(ans)