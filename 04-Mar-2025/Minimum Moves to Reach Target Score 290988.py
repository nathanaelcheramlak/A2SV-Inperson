# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while target > 1:
            if target % 2 == 0 and maxDoubles != 0:
                target //= 2
                count += 1
                maxDoubles -= 1
            else:
                count += 1
                target -= 1
            
            if maxDoubles == 0:
                return count + target - 1
        
        return count