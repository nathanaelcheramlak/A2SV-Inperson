# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direction = -1 # backward
        idx = 1
        while time:
            if idx == n or idx == 1:
                direction *= -1
            idx += direction
            time -= 1
        return idx