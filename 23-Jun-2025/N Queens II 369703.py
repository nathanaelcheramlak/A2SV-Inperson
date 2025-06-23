# Problem: N Queens II - https://leetcode.com/problems/n-queens-ii/

class Solution:
    def totalNQueens(self, n: int) -> int:
        solution_count = 0
        col_set = set()
        forward_set = set()
        backward_set = set()

        def find_position(row, col):
            nonlocal solution_count
            if row == n and col == n:
                solution_count += 1

            if col == n:
                return
            
            # Place the queen
            if col not in col_set and (row + col) not in forward_set and (row - col) not in backward_set:
                col_set.add(col)
                forward_set.add(row + col)
                backward_set.add(row - col)

                find_position(row + 1, 0)

                col_set.discard(col)
                forward_set.discard(row + col)
                backward_set.discard(row - col)

            # Don't place the queen
            find_position(row, col + 1)
        
        find_position(0, 0)
        return solution_count