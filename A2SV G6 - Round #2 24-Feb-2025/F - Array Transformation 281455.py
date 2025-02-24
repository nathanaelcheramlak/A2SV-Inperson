# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    frequency = Counter(arr)
    frequency = dict(sorted(frequency.items(), key=lambda x: x[1]))

    ans = n
    remaining = len(frequency)

    for freq in frequency.values():
        ans = min(ans, n - (freq * remaining))
        remaining -= 1
    
    print(ans)

