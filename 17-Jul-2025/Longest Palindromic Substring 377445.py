# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = s[0]
        for i in range(1, n):
            # Odd
            left = i - 1
            right = i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            if len(longest) < right - left - 1:
                longest = s[left + 1: right]

            # Even
            left = i - 1
            right = i
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            if len(longest) < right - left - 1:
                longest = s[left + 1: right]
        
        return longest