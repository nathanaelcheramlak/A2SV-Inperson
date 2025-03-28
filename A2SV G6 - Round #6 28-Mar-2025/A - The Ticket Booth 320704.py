# Problem: A - The Ticket Booth - https://codeforces.com/gym/594077/problem/A

from math import ceil
n, m = map(int, input().split())

print(ceil(m / n))