# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    i = count = 0
    while i < n - 1:
        if arr[i] > arr[i + 1]:
            count += 1
            i += 1
        i += 1
    
    print(count)