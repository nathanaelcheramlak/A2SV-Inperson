# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        for me in s:
            if me == '(':
                stack.append(score)
                score = 0
            else:
                score = stack.pop() + max(score * 2, 1)
        
        return score