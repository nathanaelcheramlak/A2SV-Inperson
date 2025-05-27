# Problem: Arranging Coins - https://leetcode.com/problems/arranging-coins/description/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        coin = 1
        while n > 0:
            if n - coin > 0:
                count += 1
                n -= coin
                coin += 1
            else:
                break
        return count