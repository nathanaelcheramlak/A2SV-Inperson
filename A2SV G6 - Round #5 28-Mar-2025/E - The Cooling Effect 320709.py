# Problem: E - The Cooling Effect - https://codeforces.com/gym/591928/problem/E

from collections import defaultdict
for _ in range(int(input())):
    input()
    n, k = map(int, input().split())
    pos = list(map(int, input().split()))
    val = list(map(int, input().split()))
    m = dict()

    for i in range(k):
        m[pos[i] - 1] = val[i]
    
    ans = [float('inf')] * (n)

    # Forward
    temp = float('inf')
    for i in range(n):
        if i in m and m[i] < temp + 1:
            temp = m[i]
        else:
            temp += 1
        ans[i] = temp
    
    # Backward
    temp = ans[-1]
    for i in range(n-1, -1, -1):
        if i in m and m[i] < temp + 1:
            temp = m[i]
        else:
            temp += 1
        ans[i] = min(temp, ans[i])
    
    print(*ans)
