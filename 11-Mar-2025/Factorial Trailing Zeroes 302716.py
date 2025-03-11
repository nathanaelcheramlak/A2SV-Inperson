# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        # Recursive Spree
        def fact(n):
            if n == 0:
                return 1
            return n * fact(n - 1)
        
        def rem(f):
            if f % 10 != 0:
                return 0
            return 1 + rem(f//10)
            
        ans = rem(fact(n))      
        return ans