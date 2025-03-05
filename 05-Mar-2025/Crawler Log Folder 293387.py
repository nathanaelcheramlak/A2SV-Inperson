# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        op_needed = 0
        for log in logs:
            if log == '../':
                op_needed = max(0, op_needed - 1)
            elif log != './':
                op_needed += 1
        
        return op_needed