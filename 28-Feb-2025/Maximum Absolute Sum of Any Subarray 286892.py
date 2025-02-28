# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Kadanes Algorithm
        p = 0
        n = 0
        posetive_max = 0
        negative_max = 0
        for i in range(len(nums)):
            posetive_max += nums[i]
            negative_max -= nums[i]

            posetive_max = max(posetive_max, nums[i])
            negative_max = max(negative_max, 0)

            p = max(posetive_max, p)
            n = max(negative_max, n)

        ans = max(p, n)
        return ans
        