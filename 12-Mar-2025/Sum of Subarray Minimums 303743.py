# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        less_left = [-1] * n
        less_right = [n] * n
        stack = [] # monotonic increasing stack

        # less_left
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            less_left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []
        # less_right
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            less_right[i] = stack[-1] if stack else n
            stack.append(i)

        # Magic happens (calculating the sum)
        total = 0
        for i in range(n):
            total += arr[i] * (i - less_left[i]) * (less_right[i] - i)
        
        return total % (10 ** 9 + 7)
