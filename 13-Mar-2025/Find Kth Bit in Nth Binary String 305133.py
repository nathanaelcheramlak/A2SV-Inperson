# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def rec(n, k, s=['0']):
            if k <= len(s):
                return s[k - 1]
            l = len(s) - 1
            s.append('1')
            for i in range(l, -1, -1):
                s.append('0' if s[i] == '1' else '1')
            return rec(n, k, s)
        
        return rec(n, k)
