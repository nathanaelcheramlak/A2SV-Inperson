# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Stores Value and Index from nums 
        value_index = dict()

        for i in range(len(nums)):
            difference = target - nums[i]

            # Checks if the difference exists, and if it does we have found the two numbers.
            if difference in value_index:
                return [i, value_index[difference]]

            # If the above condition fail, we will add a new element to our dictionary above.
            value_index[nums[i]] = i
        return []