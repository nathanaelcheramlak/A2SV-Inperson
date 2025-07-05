# Problem: Sudoku Solver - https://leetcode.com/problems/sudoku-solver/description/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def get_box_number(i, j):
            row = i // 3
            col = j // 3
            return 3 * row + col
            
        row_dict = defaultdict(set)
        col_dict = defaultdict(set)
        box_dict = defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if board[i][j] != '.':
                    box_number = get_box_number(i, j)
                    row_dict[i].add(val)
                    col_dict[j].add(val)
                    box_dict[box_number].add(val)

        def solve(i, j):
            if i == 8 and j == 9:
                return True
            if j == 9 and i < 8:
                return solve(i + 1, 0)
            if board[i][j] != '.':
                return solve(i, j + 1)
            
            for val in range(1, 10):
                box_no = get_box_number(i, j)
                val = str(val)
                if val in row_dict[i] or val in col_dict[j] or val in box_dict[box_no]:
                    continue
                row_dict[i].add(val)
                col_dict[j].add(val)
                box_dict[box_no].add(val)
                board[i][j] = val
                if solve(i, j + 1):
                    return True
                board[i][j] = '.'
                row_dict[i].discard(val)
                col_dict[j].discard(val)
                box_dict[box_no].discard(val)   

            return False
        solve(0, 0)

                        