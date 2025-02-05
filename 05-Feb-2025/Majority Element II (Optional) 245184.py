# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        _map = Counter(nums)
        N = len(nums)
        return [key for key, val in _map.items() if val > (N / 3)]