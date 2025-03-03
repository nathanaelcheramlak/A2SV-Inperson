# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        perimeter = 0
        for i in range(len(nums) - 2):
            # Check if its a valid triangle side
            if nums[i] < nums[i + 1] + nums[i + 2]:
                perimeter = max(perimeter, nums[i] + nums[i + 1] + nums[i + 2])
        
        return perimeter