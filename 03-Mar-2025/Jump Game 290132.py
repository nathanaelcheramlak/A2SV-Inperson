# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        farthest = 0
        for i in range(len(nums)):
            if farthest < i:
                return False
            farthest = max(farthest, nums[i] + i)

        return True