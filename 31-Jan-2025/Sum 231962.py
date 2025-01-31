# Problem: Sum - https://codeforces.com/contest/1742/problem/A

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if a + c == b or a + b == c or b + c == a:
        print("YES")
    else:
        print("NO")