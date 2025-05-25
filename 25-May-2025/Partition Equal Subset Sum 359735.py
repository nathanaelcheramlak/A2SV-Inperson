# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False  # Early exit if odd sum
        
        target = total_sum // 2
        cache = {}
        
        def backtrack(i, remaining_sum):
            if remaining_sum == 0:
                return True
            if i >= len(nums) or remaining_sum < 0:
                return False
            
            if (i, remaining_sum) in cache:
                return cache[(i, remaining_sum)]

            cache[(i, remaining_sum)] = backtrack(i + 1, remaining_sum - nums[i]) or backtrack(i + 1, remaining_sum)
            return cache[(i, remaining_sum)]
        
        return backtrack(0, target)