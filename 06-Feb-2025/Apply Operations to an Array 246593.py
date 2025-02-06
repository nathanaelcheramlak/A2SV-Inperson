# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # Apply the operation
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        # Shift the zeros
        result = []
        for num in nums:
            if num != 0:
                result.append(num)
        result.extend([0] * (len(nums) - len(result)))
        return result