# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if not s or len(s) == 1:
            return ''
        
        sets = set(s)
        for i, letter in enumerate(s):
            if letter.lower() not in sets or letter.upper() not in sets:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i + 1:])
                if len(left) >= len(right):
                    return left
                return right
        
        return s
