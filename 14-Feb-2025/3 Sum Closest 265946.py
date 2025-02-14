# Problem: 3 Sum Closest - https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')

        for idx in range(len(nums) - 2):
            num = nums[idx]
            left = idx + 1
            right = len(nums) - 1
            current_sum = num + nums[left] + nums[right]

            while right > left:
                current_sum = num + nums[left] + nums[right]
                if abs(closest - target) >= abs(current_sum - target):
                    closest = current_sum
                if current_sum > target:
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    return target
        
        return closest
            