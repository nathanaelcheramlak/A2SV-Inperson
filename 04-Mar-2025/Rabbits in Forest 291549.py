# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

from math import ceil

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        n = len(answers)
        color = Counter(answers)
        ans = 0
        for k, val in color.items():
            ans += ceil(val / (k + 1)) * (k + 1)
        
        return ans