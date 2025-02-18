# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        right = 1
        for i in range(n-1, -1, -1):
            output[i] *= right
            right *= nums[i]

        left = 1
        for i in range(n):
            output[i] *= left
            left *= nums[i]
            
        return output