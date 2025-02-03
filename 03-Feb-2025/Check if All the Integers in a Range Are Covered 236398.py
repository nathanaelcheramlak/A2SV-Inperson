# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        my_set = set()
        for interval in ranges:
            l, r = interval
            for i in range(l, r + 1):
                my_set.add(i)
        
        for i in range(left, right + 1):
            if i not in my_set:
                return False
        
        return True
