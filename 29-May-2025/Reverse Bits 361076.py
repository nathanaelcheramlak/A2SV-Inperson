# Problem: Reverse Bits - https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        num = 0
        for i in range(32):
            bit =  int((1 << i) & n != 0)
            num |= bit << (31 - i)
        return num