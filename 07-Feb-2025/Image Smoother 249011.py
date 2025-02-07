# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        row = len(M)
        col = len(M[0])
        smoothed = [[None] * col for _ in range(row)]

        def inbound(i, j):
            return 0 <= i < row and 0 <= j < col
        
        for i in range(row):
            for j in range(col):
                grid_size = 1
                current_sum = M[i][j]
                if inbound(i-1, j-1):
                    current_sum += M[i-1][j-1]
                    grid_size += 1
                if inbound(i-1, j):
                    current_sum += M[i-1][j]
                    grid_size += 1
                if inbound(i-1, j+1):
                    current_sum += M[i-1][j+1]
                    grid_size += 1
                if inbound(i, j-1):
                    current_sum += M[i][j-1]
                    grid_size += 1
                if inbound(i, j+1):
                    current_sum += M[i][j+1]
                    grid_size += 1
                if inbound(i+1, j-1):
                    current_sum += M[i+1][j-1]
                    grid_size += 1
                if inbound(i+1, j):
                    current_sum += M[i+1][j]
                    grid_size += 1
                if inbound(i+1, j+1):
                    current_sum += M[i+1][j+1]
                    grid_size += 1
                
                smoothed[i][j] = current_sum // grid_size
        
        return smoothed
