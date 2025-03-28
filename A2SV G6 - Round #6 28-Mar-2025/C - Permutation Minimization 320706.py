# Problem: C - Permutation Minimization - https://codeforces.com/gym/594077/problem/C

from collections import deque

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    q = deque()
    q.append(nums[0])
    left = nums[0]
    for i in range(1, n):
        if nums[i] < left:
            q.appendleft(nums[i])
            left = nums[i]
        else:
            q.append(nums[i])
    
    print(*q)