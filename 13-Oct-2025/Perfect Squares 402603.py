# Problem: Perfect Squares - https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        squares = set(i ** 2 for i in range(1, 101))
        dp = [float('inf') for i in range(n + 1)]
        for i in range(1, n + 1):
            if i in squares:
                dp[i] = 1
                continue
            for j in range(1, int(i ** 0.5) + 1):
                dp[i] = min(dp[i], 1 + dp[i - j*j])

        return dp[n]