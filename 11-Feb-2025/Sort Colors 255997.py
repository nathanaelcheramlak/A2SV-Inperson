# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = len(nums) - 1
        p = 0
        while p2 >= p:
            if nums[p] == 0:
                nums[p1], nums[p] = nums[p], nums[p1]
                p1 += 1
            elif nums[p] == 2:
                nums[p2], nums[p] = nums[p], nums[p2]
                p2 -= 1
                p -= 1

            p += 1 
        

        