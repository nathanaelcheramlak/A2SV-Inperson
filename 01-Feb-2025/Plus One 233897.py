# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(str(digit) for digit in digits))
        num += 1
        ans = [int(n) for n in str(num)]
        return ans