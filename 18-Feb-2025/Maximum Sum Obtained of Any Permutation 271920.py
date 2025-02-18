# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        for start, end in requests:
            prefix[start] += 1
            prefix[end + 1] -= 1

        # Calculate the prefix sum
        for i in range(1, n):
            prefix[i] = prefix[i] + prefix[i - 1]
        
        prefix.pop()
        prefix.sort()
        nums.sort()
        total_sum = 0
        for i in range(n):
            product = prefix[i] * nums[i]
            total_sum += product
        
        return total_sum % (10 ** 9 + 7)
