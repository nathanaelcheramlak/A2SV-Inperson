# Problem: Palindrome Number - https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        reverse = 0
        store = x
        while x > 0:
            reverse = (10 * reverse) + x % 10
            x //= 10

        return reverse == store