# Problem: Rotate String - https://leetcode.com/problems/rotate-string/

class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        return goal in (s + s) and len(s) == len(goal)
        