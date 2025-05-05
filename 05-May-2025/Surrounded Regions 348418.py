# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        N = len(board)
        M = len(board[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def inbound(i, j):
            return 0 <= i < N and 0 <= j < M

        def free_o(i, j):
            board[i][j] = 'o'
            for x, y in directions:
                r, c = i + x, j + y
                if inbound(r, c) and board[r][c] == 'O':
                    free_o(r, c)


        for i in range(N):
            for j in range(M):
                if (i == 0 or i == N - 1 or j == 0 or j == M - 1) and board[i][j] == 'O':
                    free_o(i, j)
        
        for i in range(N):
            for j in range(M):
                if board[i][j] == 'o':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
