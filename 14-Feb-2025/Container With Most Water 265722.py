# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_volume = 0
        left = 0
        right = len(height) - 1

        while right > left:
            min_height = min(height[left], height[right])
            volume = min_height * (right - left)
            max_volume = max(max_volume, volume)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_volume