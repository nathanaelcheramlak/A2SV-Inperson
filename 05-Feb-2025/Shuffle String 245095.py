# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        N = len(s)
        result = [None] * N

        for i in range(N):
            idx = indices[i]
            val = s[i]

            result[idx] = val

        return ''.join(result)
