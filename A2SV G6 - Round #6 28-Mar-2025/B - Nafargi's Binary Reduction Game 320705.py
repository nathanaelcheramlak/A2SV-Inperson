# Problem: B - Nafargi's Binary Reduction Game - https://codeforces.com/gym/594077/problem/B

from collections import Counter
n = int(input())
binary = list(map(str, input().strip()))

count = Counter(binary)
print(abs(count['0'] - count['1']))