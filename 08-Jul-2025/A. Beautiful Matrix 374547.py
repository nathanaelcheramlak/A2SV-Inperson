# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

i = 0
l = 0

count = 0
for j in range(5):
    row = list(map(int, input().split()))
    if 1 in row:
        one = row.index(1)
        i = abs(2 - one)
        l = abs(2 - j)

print(i + l)