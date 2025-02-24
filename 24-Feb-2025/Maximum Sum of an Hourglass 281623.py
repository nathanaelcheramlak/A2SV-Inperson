# Problem: Maximum Sum of an Hourglass - https://leetcode.com/problems/maximum-sum-of-an-hourglass/

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        def inbound(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])

        # Calcualate Prefix Sum
        for i in range(len(grid)):
            acc = 0
            row = [0]
            for num in grid[i]:
                acc += num
                row.append(acc)
            grid[i] = row

        maxima = 0
        for i in range(2, len(grid)):
            for j in range(3, len(grid[0])):
                top = grid[i - 2][j] - grid[i - 2][j - 3]
                bottom = grid[i][j] - grid[i][j - 3]
                mid = grid[i - 1][j - 1] - grid[i - 1][j - 2]

                hour_glass = top + bottom + mid
                maxima = max(hour_glass, maxima)
        
        return maxima
