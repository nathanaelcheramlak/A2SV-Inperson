# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def check(force):
            ball = 1
            last_ball = position[0] 
            for i in range(1, len(position)):
                if last_ball + force <= position[i]:
                    last_ball = position[i]
                    ball += 1
                    
                if ball >= m:
                    return True
            return ball >= m

        
        left = 0
        right = max(position)
        while right - left > 1:    
            mid = left + (right - left) // 2
            if check(mid):
                left = mid 
            else:
                right = mid
        
        return left 