# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = list()
        arr = [0] * (101)

        for num in nums:
            arr[num] += 1

        # Prefix Sum
        for idx, num in enumerate(arr):
            if idx != 0:
                arr[idx] = arr[idx - 1] + arr[idx]
        
        for num in nums:
            if num == 0:
                ans.append(0)
            else:
                ans.append(arr[num - 1])
        
        return ans