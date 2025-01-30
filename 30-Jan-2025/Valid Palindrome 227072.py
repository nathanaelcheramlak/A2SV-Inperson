# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        h = list()
        for l in s:
            if l.isalnum():
                h.append(l.lower())

        return h == h[::-1]