# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = []
        idx = 0
        minLen = min(len(s) for s in strs)
        while idx < minLen:
            current = strs[0][idx]
            for word in strs:
                if word[idx] != current:
                    return "".join(common)
            common.append(current)
            idx += 1
        return "".join(common)