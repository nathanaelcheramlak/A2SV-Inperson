# Problem: Sqrt(x) - https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while right > left:
            mid = left + (right - left) // 2 + 1
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid
        
        return left