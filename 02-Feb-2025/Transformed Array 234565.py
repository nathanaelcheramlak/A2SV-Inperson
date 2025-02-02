# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = []

        for i in range(len(nums)):
            ans.append(nums[(i + nums[i]) % N])
        
        return ans