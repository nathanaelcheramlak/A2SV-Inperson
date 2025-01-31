# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/

class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """        
        digit = ''.join(str(ord(char) - 96) for char in s)

        for _ in range(k):
            s = 0
            for d in digit:
                s += int(d)
            digit = str(s)

        return int(digit)
