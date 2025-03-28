# Problem: D - Meklit's Chat Screen - https://codeforces.com/gym/594077/problem/D

from collections import deque, defaultdict

n, k = map(int, input().split())
chats = list(map(int, input().split()))

q = deque()
s = defaultdict(int)

for i in range(min(n, k)):
    if chats[i] not in s:
        s[chats[i]] += 1
        q.append(chats[i])

for i in range(k,  n):
    if chats[i] not in s:
        s[chats[i]] += 1
        q.append(chats[i])
    if len(q) > k:
        left = q.popleft()
        s[left] -= 1
        if s[left] == 0:
            del s[left]

q = list(q)[::-1]
print(len(q))
print(*q)