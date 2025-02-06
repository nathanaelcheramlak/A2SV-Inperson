# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

from collections import defaultdict
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    matrix = []

    # Receive Input
    for i in range(n):
        matrix.append(list(map(int, input().split())))

    # Helper function
    def inbound(i, j):
        return 0 <= i < n and 0 <=j < m
    
    # To store the sums of the diagonals
    backward_sum_cache = defaultdict()
    forward_sum_cache = defaultdict()

    total_max = 0

    for i in range(n):
        for j in range(m):
            backward_sum = 0
            forward_sum = 0

            # '\' (backward) sum
            if i < j:
                r, c = 0, j - i
            else:
                r, c = i - j, 0
            
            r_temp, c_temp = r, c
            
            if (r, c) not in backward_sum_cache:
                while inbound(r, c):
                    backward_sum += matrix[r][c]
                    r += 1
                    c += 1
                backward_sum_cache[(r_temp, c_temp)] = backward_sum
            else:
                backward_sum = backward_sum_cache[(r, c)]

            # '/' (forward) sum
            if i + j >= m:
                r, c = i + j - m + 1, m - 1
            else:
                r, c = 0, i + j
            
            r_temp, c_temp = r, c
            
            if (r, c) not in forward_sum_cache:
                while inbound(r, c):
                    forward_sum += matrix[r][c]
                    r += 1
                    c -= 1
                forward_sum_cache[(r_temp, c_temp)] = forward_sum
            else:
                forward_sum = forward_sum_cache[(r, c)]
            
            total_max = max(total_max, forward_sum + backward_sum - matrix[i][j])
    
    print(total_max)