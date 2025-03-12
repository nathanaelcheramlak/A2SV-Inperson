# Problem: Largest Rectangle in Histogram (Optional) - https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        area = 0
        min_stack = [] # increasing
        for i, h in enumerate(heights):
            while min_stack and heights[min_stack[-1]] > h:
                height = heights[min_stack.pop()]
                w = i if not min_stack else i - min_stack[-1] - 1
                area = max(area, height * w)
            min_stack.append(i)

        while min_stack:
            h = heights[min_stack.pop()]
            w = n if not min_stack else n - min_stack[-1] - 1
            area = max(area, h * w)
        
        return area