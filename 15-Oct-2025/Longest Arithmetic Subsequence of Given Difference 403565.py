# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        seen = defaultdict(int)
        for num in arr:
            target = num - difference
            if target in seen:
                seen[num] = seen[target] + 1
            else:
                seen[num] = 1
        
        return max(seen.values())