# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        # Seeker and Placeholder
        step_count = 0
        black_count = 0
        for ball in s:
            if ball == "1":
                black_count += 1
            else:
                step_count += black_count
        
        return step_count
        
