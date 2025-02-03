# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        total = (N * (N + 1)) // 2
        current = sum(nums)

        return total - current