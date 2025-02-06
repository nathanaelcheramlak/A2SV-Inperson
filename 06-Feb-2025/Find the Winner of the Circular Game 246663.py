# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        s = 0
        for i in range(n):
            s = (s + k) % (i + 1)
        
        return s + 1
        