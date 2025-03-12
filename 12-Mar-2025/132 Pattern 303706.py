# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        stack = [] # monotonic stack (decreasing) {j}
        k = float(-inf) # tracks {k}

        for i in range(n - 1, -1, -1):
            if nums[i] < k:
                return True
            while stack and stack[-1] < nums[i]:
                k = stack.pop()
            stack.append(nums[i])
        
        return False