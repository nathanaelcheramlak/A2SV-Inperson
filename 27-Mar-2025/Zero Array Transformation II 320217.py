# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if all(num == 0 for num in nums):
            return 0
        def check(k):
            prefix = [0] * len(nums)
            for l, r, val in queries[:k]:
                prefix[l] += val
                if r + 1 < len(nums):
                    prefix[r + 1] -= val
            acc = 0
            for i in range(len(nums)):
                acc += prefix[i]
                prefix[i] = acc

            for i in range(len(nums)):
                if prefix[i] < nums[i]:
                    return False
            return True
        
        left = 0
        right = len(queries) 
        res = -1
        while right >= left:
            mid = left + (right - left) // 2 
            if check(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res

            
