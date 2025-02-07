# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row, col = len(mat), len(mat[0])
        diagonal = list()

        def inbound(i, j):
            return 0 <= i < row and 0 <= j < col

        r, c = 0, 0
        x, y = 1, 0
        while True:
            diag = list()
            i, j = r, c
            while inbound(i, j):
                diag.append(mat[i][j])
                i -= 1
                j += 1
            
            if not inbound(r, c) and (x, y) == (1, 0):
                r, c = r - x, c - y
                x, y = 0, 1
            if not inbound(r, c) and (x, y) != (1, 0):
                break

            r, c = r + x, c + y
            if (i + j) % 2 != 0: 
                diagonal.extend(diag[::-1])
            else:
                diagonal.extend(diag)
        
        return diagonal