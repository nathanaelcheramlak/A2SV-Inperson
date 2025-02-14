# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_count = 0
        left = 0
        max_length = 0
        for right in range(len(nums)):
            # Next element
            if nums[right] == 0:
                zero_count += 1

            while zero_count > k: # If Invalid make it valid
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
        
        return max_length
