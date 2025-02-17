# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # Initialize the matrix and compute prefix sums directly
        rows, cols = len(matrix), len(matrix[0])
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)] #To prevent out-of-bound errors
        
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                self.prefix[i][j] = (
                    matrix[i - 1][j - 1] +
                    self.prefix[i - 1][j] +
                    self.prefix[i][j - 1] -
                    self.prefix[i - 1][j - 1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Use the precomputed prefix sum matrix to get the result in O(1)
        return (
            self.prefix[row2 + 1][col2 + 1] -
            self.prefix[row2 + 1][col1] -
            self.prefix[row1][col2 + 1] +
            self.prefix[row1][col1]
        )
