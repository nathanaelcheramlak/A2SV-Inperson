# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def backtrack(total):
            if total > amount:
                return float('inf')
            if total == amount:
                return 0
            if total in cache:
                return cache[total]
            
            temp = float('inf')
            for coin in coins:
                if coin + total > amount:
                    continue
                temp = min(temp, 1 + backtrack(total + coin))
            cache[total] = temp
            return temp
        
        ans = backtrack(0)
        if ans != float('inf'):
            return ans
        return -1