# Problem: Divisibility by 2^n - https://codeforces.com/contest/1744/problem/D

def multiple_counter(n):
    multiple_count = {1: 0}
    for i in range(2, n + 1, 2):
        count = 0
        temp = i
        while temp > 1:
            if temp & 1:
                break
            if temp in multiple_count:
                count += multiple_count[temp]
                break
            count += 1
            temp //= 2

        multiple_count[i] = count

    return dict(sorted(multiple_count.items(), key=lambda x: x[1], reverse=True))

def findtwo(n):
    count = 0
    while n > 1:
        if n & 1:
            break
        n //= 2
        count += 1
    return count

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    for num in arr:
        n -= findtwo(num)
        if n <= 0:
            return 0
    count = 0
    multiple_count = multiple_counter(len(arr))
    for _, val in multiple_count.items():
        if n <= 0:
            return count
        count += 1
        n -= val
    return -1 if n != 0 else count

for _ in range(int(input())):
    print(solve())    
        
