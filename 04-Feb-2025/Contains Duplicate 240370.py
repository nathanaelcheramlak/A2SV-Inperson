# Problem: Contains Duplicate - https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))