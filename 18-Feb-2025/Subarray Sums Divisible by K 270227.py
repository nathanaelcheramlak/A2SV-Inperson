# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_dict = {0: 1}
        running_sum = 0
        ans = 0

        for idx, num in enumerate(nums):
            running_sum += num
            if (running_sum % k) in remainder_dict:
                ans += remainder_dict[running_sum % k]
            
            remainder_dict[running_sum % k] = remainder_dict.get(running_sum % k, 0) + 1
        
        return ans