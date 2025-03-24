# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B

from collections import defaultdict, deque
import sys
n = int(input())

adj = defaultdict(list)
for i in range(n - 1):
    par = int(input())
    adj[par].append(i + 2)

level = [1]
while level:
    new_level = []
    for node in level:
        leaf_count = 0
        for child in adj[node]:
            if child not in adj:
                leaf_count += 1
            else:
                new_level.append(child)

        if leaf_count < 3:
            print("No")
            sys.exit(0)
    level = new_level

print('Yes')

