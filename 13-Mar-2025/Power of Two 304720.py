# Problem: Power of Two - https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:   
        if n <= 0:
            return False         
        def two(n):
            if n % 2 != 0:
                return n
            return two(n // 2)
        return two(n) == 1