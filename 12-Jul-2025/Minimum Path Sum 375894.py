# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        # Bottom Up
        grid = grid[::-1]
        dp_row = list(itertools.accumulate(grid[0][::-1]))[::-1]
        for i in range(1, row):
            new_row = [grid[i][col - 1] + dp_row[col - 1]]
            for j in range(col - 2, -1, -1):
                val = grid[i][j]
                new_row.append(min(new_row[-1], dp_row[j]) + val)
            dp_row = new_row[::-1]
        return dp_row[0]