# Problem: C - Binary Flip - https://codeforces.com/gym/590053/problem/C

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().strip()))
    b = list(map(int, input().strip()))
    
    left = -1
    difference = 0
    one_count = 0
    can_be_flipped = True
    for i in range(n):
        one_count += a[i]
        difference += a[i] ^ b[i]
        
        if one_count * 2 == i + 1:
            if difference != 0 and difference != i - left:
                can_be_flipped = False
                break
            difference = 0
            left = i

    if (difference != 0 and difference != n - left) or not can_be_flipped:
        print("NO")
    else:
        print("YES")
        