# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        running_dict = {0: 1}
        running_sum = 0
        answer = 0
        
        for num in nums:
            running_sum += num
            val = running_sum - goal
            if val in running_dict:
                answer += running_dict[val]
            running_dict[running_sum] = running_dict.get(running_sum, 0) + 1
        
        return answer