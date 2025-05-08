# Problem: N-Queens - https://leetcode.com/problems/n-queens/description/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        cols = set()
        forward = set()
        backward = set()

        def queen(path , row , col):
            if row == n:
                res = list(''.join(row) for row in path)
                ans.append(res)
                return

            if col == n:
                return

            # Pick
            if row + col not in forward and col not in cols and row - col not in backward:
                path[row][col] = 'Q'

                cols.add(col)
                forward.add(row + col)
                backward.add(row - col)

                queen(path, row + 1, 0)

                path[row][col] = '.'
                
                cols.discard(col)
                forward.discard(row + col)
                backward.discard(row - col)

            # No Pick
            queen(path, row, col + 1)

        queen([['.' for _ in range(n)] for i in range(n)], 0, 0)
        return ans
        