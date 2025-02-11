# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        count = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
        ans = []
        for key, val in count.items():
            ans.extend([key] * val)
        
        return ''.join(ans)