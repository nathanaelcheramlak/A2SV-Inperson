# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

n, m = map(int, input().split())

for i in range(n):
    if (i + 1) % 2 == 1:
        print('#' * m)
    else:
        if (i + 1) % 4 == 0:
            print('#' + '.' * (m - 1))
        else:
            print('.' * (m - 1) + '#')