# Problem: Subarray Product Less Than K - https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        ans = 0
        product = 1

        for right in range(len(nums)):
            product *= nums[right]
            while left < right and product >= k:
                product //= nums[left]
                left += 1
            if product < k:
                ans += right - left + 1
        
        return ans