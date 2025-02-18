# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum_sum  = float("-inf")
        running_sum = 0

        for num in nums:
            running_sum += num
            running_sum = max(num, running_sum)
            maximum_sum = max(maximum_sum, running_sum)
        return maximum_sum