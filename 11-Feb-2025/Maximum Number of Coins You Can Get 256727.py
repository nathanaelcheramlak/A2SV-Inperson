# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i = len(piles) // 3
        ans = 0
        while i < len(piles):
            ans += piles[i]
            i += 2
        return ans