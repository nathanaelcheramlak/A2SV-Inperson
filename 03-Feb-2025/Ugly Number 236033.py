# Problem: Ugly Number - https://leetcode.com/problems/ugly-number/description/

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n >= 1:
            if n % 5 == 0:
                n //= 5
            elif n % 3 == 0:
                n //= 3
            elif n % 2 == 0:
                n //= 2
            else:
                break
        
        return n == 1