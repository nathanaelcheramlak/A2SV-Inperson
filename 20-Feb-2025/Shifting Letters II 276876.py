# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        arr = [0] * (n + 1) # The last element is useless its there to prevent out of bound errors

        for left, right, direction in shifts:
            if direction == 0: # Shift backward
                arr[left] -=  1
                arr[right + 1] += 1
            else: # Shift forward
                arr[left] += 1
                arr[right + 1] -= 1

        # Prefix summer
        for i in range(1, n):
            arr[i] += arr[i - 1]

        result = ''
        for i in range(n):
            result += (chr((ord(s[i]) + arr[i] - 97) % 26 + 97))

        return result
            