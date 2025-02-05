# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # Array Index Marking 
        ans = list()
        for num in nums:
            i = abs(num) - 1
            if nums[i] > 0:
                nums[i] *= -1
            else:
                ans.append(abs(num))

        return ans


