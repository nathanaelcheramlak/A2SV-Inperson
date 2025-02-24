# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

from collections import Counter
t = int(input())
for _ in range(t):
    row = int(input())
    col = row
    matrix = list()
    answer = 0

    for _ in range(row):
        matrix.append(list(map(int, input().strip())))
    
    mat9 = list(list(x) for x in zip(*matrix[::-1]))
    mat18 = list(list(x) for x in zip(*mat9[::-1]))
    mat27 = list(list(x) for x in zip(*mat18[::-1]))

    for i in range(row):
        for j in range(col):
            x = matrix[i][j] + mat9[i][j] + mat18[i][j] + mat27[i][j]
            if x == 1 or x == 3:
                answer += 1
            elif x == 2:
                answer += 2
    
    print(answer // 4)
