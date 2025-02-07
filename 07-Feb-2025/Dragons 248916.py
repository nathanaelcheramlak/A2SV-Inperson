# Problem: Dragons - https://codeforces.com/problemset/problem/230/A

s, n = map(int, input().split())
strength = list()

for _ in range(n):
    strength.append(list(map(int, input().split())))

strength.sort()
total_strength = s

for dragon_strength, bonus_strength in strength:
    if total_strength <= dragon_strength:
        print("NO")
        break
    else:
        total_strength += bonus_strength
else:
    print("YES")