# Problem: Smallest Even Multiple - https://leetcode.com/problems/smallest-even-multiple/

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 1:
            return n * 2
        return n