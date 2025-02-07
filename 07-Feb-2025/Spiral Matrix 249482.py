# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        spiral_matrix = list()
        seen_set = set()

        def inbound(i, j):
            return 0 <= i < row and 0 <= j < col

        direction_map = {(0,1):(1,0), (1,0):(0,-1), (0,-1):(-1,0), (-1,0):(0,1)}

        i, j = 0, 0
        x, y = 0, 1 # Initailly we run to the right. They represent the direction
        while True:
            if (i, j) in seen_set:
                break

            if inbound(i, j):
                spiral_matrix.append(matrix[i][j])
                seen_set.add((i, j))

            if not inbound(i + x, j + y) or (i + x, j + y) in seen_set: # Change direction
                x, y = direction_map[(x, y)]
            i, j = i + x, j + y
        
        return spiral_matrix
                    