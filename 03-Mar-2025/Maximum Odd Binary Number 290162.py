# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = Counter(s)
        return ''.join(['1'] * (count['1'] - 1) + ['0'] * count['0'] + ['1'])
