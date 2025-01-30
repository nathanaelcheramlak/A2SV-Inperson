# Problem: Number of Good Pairs - https://leetcode.com/problems/number-of-good-pairs/

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map = dict()
        res = 0

        for num in nums:
            if num not in map:
                map[num] = 0
            else:
                map[num] += 1
                res += map[num]
        
        return res