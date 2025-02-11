# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)

        for i in range(n):
            swapped = False
            for j in range(n - i - 1):
                if str(nums[j]) + str(nums[j+1]) < str(nums[j+1]) + str(nums[j]):
                    nums[j], nums[j+1] = str(nums[j+1]), str(nums[j])
                    swapped = True
            if not swapped:
                break        
        
        nums = ''.join([str(x) for x in nums])
        if int(nums) == 0:
            return '0'

        return nums