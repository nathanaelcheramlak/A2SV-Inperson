# Problem: Contiguous Array - https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        running_dict = defaultdict(int)
        running_dict[0] = -1
        running_sum = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                running_sum += 0.5
            else:
                running_sum -= 0.5

            if running_sum in running_dict:
                ans = max(ans, i - running_dict[running_sum])
            if running_sum not in running_dict:
                running_dict[running_sum] = i

        return ans