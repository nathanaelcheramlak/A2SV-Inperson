# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for i in range(1 << n):
            temp = []
            for j in range(n - 1, -1, -1):
                if i & (1 << j):
                    temp.append(nums[j])
            ans.append(temp)
            
        return ans