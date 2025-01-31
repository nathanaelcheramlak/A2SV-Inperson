# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

t = int(input())
for _ in range(t):
    word = input()
    love = list('codeforces')
    count = 0
    for i in range(10):
        if love[i] != word[i]:
            count += 1
    
    print(count)