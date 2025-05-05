# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        def inbound(i, j):
            return 0 <= i < row and 0 <= j < col
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        max_area = 0
        def bfs(i, j):
            grid[i][j] = 0
            total = 1
            for x, y in directions:
                r, c = i + x, j + y
                if inbound(r, c) and grid[r][c] == 1:
                    total += bfs(r, c)

            return total
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    area = bfs(i, j)
                    max_area = max(area, max_area)
        
        return max_area