# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        mapper = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        i = 0
        while i < len(s):
            if i != len(s) - 1 and mapper[s[i]] < mapper[s[i + 1]]:
                result += (mapper[s[i + 1]] - mapper[s[i]]) 
                i += 1
            else:
                result += mapper[s[i]]
            i += 1

        return result