# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = list()
        for idx, num in enumerate(nums):
            if idx == 0:
                running_sum.append(num)
            else:
                running_sum.append(running_sum[idx - 1] + num)
        
        return running_sum