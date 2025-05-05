# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        original = image[sr][sc]

        def inbound(i, j):
            return 0 <= i < row and 0 <= j < col
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        seen = set()
        def dfs(i, j):
            seen.add((i, j))
            image[i][j] = color
            for x, y in directions:
                r, c = i + x, j + y
                if inbound(r, c) and (r, c) not in seen and image[r][c] == original:
                    dfs(r, c)
        
        dfs(sr, sc)
        return image