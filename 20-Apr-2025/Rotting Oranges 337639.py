# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        def inbound(i, j):
            return 0 <= i < row and 0 <= j < col
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        rotten = []
        fresh_count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                if grid[i][j] == 1:
                    fresh_count += 1
        
        queue = deque(rotten)
        time = 0
        while queue:
            fresh_found = False
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for x, y in directions:
                    r, c = i + x, j + y
                    if inbound(r, c) and grid[r][c] == 1:
                        fresh_found = True
                        grid[r][c] = 2
                        queue.append((r, c))
                        fresh_count -= 1

            if fresh_found:
                time += 1
            else:
                break
            
        if fresh_count == 0:
            return time
        return -1