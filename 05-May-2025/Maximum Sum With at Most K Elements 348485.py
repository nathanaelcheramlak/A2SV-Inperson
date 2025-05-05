# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        heap = []
        for i in range(len(limits)):
            row = sorted(grid[i], reverse=True)
            heap.extend(row[:limits[i]])
        heap.sort(reverse=True)
        return sum(heap[:k])