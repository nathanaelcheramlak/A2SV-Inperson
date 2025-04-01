# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

from bisect import bisect_left
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        left = 0
        right = N + 1
        while right - left > 1:
            mid = left + (right - left) // 2
            if mid <= N - bisect_left(citations, mid):
                left = mid
            else:
                right = mid
        
        return left