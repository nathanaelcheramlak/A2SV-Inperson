# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        store = ''
        stack = []
        for char in s:
            if char.isnumeric():
                num = num * 10 + int(char)
            elif char == '[':
                stack.append((store, num))
                num = 0
                store = ''
            elif char == ']':
                prev, n = stack.pop()
                store = prev + store * n
            else:
                store += char
        
        return store

