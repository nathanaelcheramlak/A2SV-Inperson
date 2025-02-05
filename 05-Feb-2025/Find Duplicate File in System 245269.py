# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        map = dict()
        
        for path in paths:
            p, *files = path.split()
            for fil in files:
                f = fil.split('(')
                content = f[1][:-1]
                directory = p + '/' + f[0]
                
                map[content] = map.get(content, [])
                map[content].append(directory)
        
        return [value for value in map.values() if len(value) > 1]