# Problem: Shifting Letters - https://leetcode.com/problems/shifting-letters/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shifts = shifts[::-1]
        prefix = [shifts[0] % 26]
        for i in range(1, len(shifts)):
            prefix.append((prefix[i - 1] + shifts[i]) % 26)

        prefix = prefix[::-1]
        answer = list()
        
        for idx, char in enumerate(s):
            shifted = chr((ord(char) - 97 + prefix[idx]) % 26 + 97)
            answer.append(shifted)
        
        return ''.join(answer)