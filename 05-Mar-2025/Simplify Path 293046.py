# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = list()
        paths = path.split('/')

        for p in paths:
            if p == '..'and stack:
                stack.pop()
            elif p != '/' and p != '.' and p != '..' and p:
                stack.append(p)
        
        return '/' + '/'.join(stack)