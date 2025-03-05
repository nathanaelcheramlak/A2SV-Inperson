# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = list()
        stack2 = list()

        for l in s:
            if l != '#':
                stack1.append(l)
            else:
                if stack1:
                    stack1.pop()

        
        for l in t:
            if l != '#':
                stack2.append(l)
            else:
                if stack2:
                    stack2.pop()

        return stack1 == stack2