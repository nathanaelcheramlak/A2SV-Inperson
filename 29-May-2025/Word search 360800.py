# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Bruteforce
        row, col = len(board), len(board[0])
        def inbound(i, j):
            return 0 <= i < row and 0 <= j < col
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def search(i, j, wordIdx, visited):
            if wordIdx == len(word):
                return 0
            if word[wordIdx] != board[i][j]:
                return 0
            visited.add((i, j))
            maxLen = 1
            for x, y in directions:
                r, c = i + x, j + y
                if inbound(r, c) and (r, c) not in visited:
                    maxLen = max(search(r, c, wordIdx + 1, visited) + 1, maxLen)
            visited.discard((i, j))
            return maxLen
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and search(i, j, 0, set()) == len(word):
                    return True
        return False