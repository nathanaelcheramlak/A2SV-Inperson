# Problem: E - Strange Mirroring - https://codeforces.com/gym/596141/problem/E

from math import log2, ceil

for _ in range(int(input())):
    s = input()
    n = len(s)
    q = int(input())
    queries = list(map(int, input().split()))

    def mirror(k):
        if k <= n:
            return s[k - 1]
        current_level = ceil(log2(k / n))
        k -= 2 ** (current_level - 1) * n
        return mirror(k).swapcase()
    
    ans = []
    for k in queries:
        ans.append(mirror(k))
    print(*ans)