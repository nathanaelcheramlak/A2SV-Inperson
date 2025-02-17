# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        running_dict = {0: 1}
        count = 0
        running_sum = 0
        for num in nums:
            running_sum += num
            if (running_sum - k) in running_dict:
                count += running_dict[running_sum - k]
            running_dict[running_sum] = running_dict.get(running_sum, 0) + 1

        return count    
