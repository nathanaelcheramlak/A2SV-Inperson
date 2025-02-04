# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        my_set = set()
        result = []
        for num in nums:
            if num in my_set:
                result.append(num)
            else:
                my_set.add(num)
        
        return result