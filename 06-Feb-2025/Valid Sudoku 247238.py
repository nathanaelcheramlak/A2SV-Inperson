# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Checks the row.
        for i in board:
            seen = set()
            for j in i:
                if j in seen:
                    return False
                if j != '.':
                    seen.add(j)

        # Checks Columns.
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] in seen:
                    return False
                if board[j][i] != '.':
                    seen.add(board[j][i])

        # Checks Boxes.
        coordinates = [(0,0), (3,0), (6,0),
                       (0,3), (3,3), (6,3),
                       (0,6), (3,6), (6,6)]
        for i, j in coordinates:
            seen = set()
            for col in range(i, i+3):
                for row in range(j, j+3):
                    item = board[col][row]
                    if item in seen:
                        return False
                    elif item != '.':
                        seen.add(item)
        return True