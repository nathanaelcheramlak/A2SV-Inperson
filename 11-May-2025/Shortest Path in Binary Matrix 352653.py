# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        if grid[0][0] or grid[row - 1][col - 1]:
            return -1
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1)]
        def inbound(i, j):
            return 0 <= i < row and 0 <= j < col
        
        level = deque([(0, 0)])
        grid[0][0] = 1
        count = 1
        while level:
            for _ in range(len(level)):
                i, j = level.popleft()
                if i == row - 1 and j == col - 1:
                    return count
                
                for x, y in directions:
                    r, c = i + x, j + y
                    if inbound(r, c) and grid[r][c] == 0:
                        grid[r][c] = 1
                        level.append((r, c))
            count += 1

        return -1