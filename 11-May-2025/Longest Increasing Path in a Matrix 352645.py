# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def inbound(i, j):
            return 0 <= i < row and 0 <= j < col

        cache = defaultdict(int)
        def dfs(r,c):
            if (r,c) in cache:
                return cache[(r,c)]

            temp = 1
            for dr,dc in directions:
                nr,nc = dr + r, dc + c
                if inbound(nr, nc) and matrix[nr][nc] > matrix[r][c]:
                    temp = max(1 + dfs(nr,nc),temp)
                    
            cache[(r,c)] = temp
            return temp

        ans = 0
        for i in range(row):
            for j in range(col):
                ans = max(ans,dfs(i,j))

        return ans