# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atleast(k):
            subarray_count = 0
            left = 0
            odd_count = 0
            for right in range(len(nums)):
                if nums[right] % 2:
                    odd_count += 1
                while odd_count >= k:
                    subarray_count += len(nums) - right
                    if nums[left] % 2:
                        odd_count -= 1
                    left += 1
            
            return subarray_count
        return atleast(k) - atleast(k + 1)