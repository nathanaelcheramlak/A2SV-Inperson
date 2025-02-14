# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import Counter, defaultdict, deque
from math import ceil, floor, gcd, inf, log2, sqrt
from cmath import inf


def iinput(): return int(input())
def sinput(): return input()
def iarray(): return list(map(int, input().split()))
def imatrix(rows): return [list(map(int,input().split())) for _ in range(rows)]
def smatrix(rows): return [input() for _ in range(rows)]
def mapint(): return map(int, input().split())

# ...
# |||
# _ _
# 0_O
# ---

def solve(nums, n, k):
    max_length = 0
    answer = []
    count = Counter()
    left = 0

    for right in range(n):
        count[nums[right]] += 1

        while len(count) > k: # Make the invalid valid
            count[nums[left]] -= 1
            if count[nums[left]] == 0:
                del count[nums[left]]
            left += 1

        if (right - left + 1) > max_length:
            max_length = max(max_length, right - left + 1)
            answer = [left + 1, right + 1]

    return answer


if __name__ == '__main__':
    # Receive input
    n, k = mapint()
    nums = iarray()

    ans = solve(nums, n, k)
    print(*ans)
    # if ans:
    #     print("YES")
    # else:
    #     print("NO")