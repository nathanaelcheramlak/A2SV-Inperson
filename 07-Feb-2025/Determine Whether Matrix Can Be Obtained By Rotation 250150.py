# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate_matrix(matrix):
            n = len(mat)
            rotated = [[0]*n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    rotated[i][j] = matrix[j][n-i-1]
            return rotated
        
        for i in range(4):
            rotated = rotate_matrix(mat)
            if rotated == target:
                return True
            mat = rotated
            
        return False