# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        root_c = int(c ** 0.5)
        a = 0
        b = root_c
        while b >= a:
            summ = (a ** 2) + (b ** 2)
            print(summ)
            if summ == c:
                return True
            elif summ > c:
                b -= 1
            else:
                a += 1
        
        return False
            