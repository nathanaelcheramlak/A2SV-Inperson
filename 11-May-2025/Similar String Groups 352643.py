# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        N = len(strs)
        in_group = [False] * N

        def find(curr_idx):
            if in_group[curr_idx]:
                return
            in_group[curr_idx] = True
            for i in range(N):
                diff = 0
                for a, b in zip(strs[curr_idx], strs[i]):
                    if a != b:
                        diff += 1
                    if diff > 2:
                        break
                else:
                    find(i)
                    in_group[i] = True
        
        count = 0
        for i in range(N):
            if not in_group[i]:
                find(i)
                count += 1

        return count