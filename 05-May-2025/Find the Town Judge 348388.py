# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = defaultdict(int)
        is_trusted = defaultdict(int)

        for a, b in trust:
            trusts[a] += 1
            is_trusted[b] += 1
        
        for person in range(1, n + 1):
            if trusts[person] == 0 and is_trusted[person] == n - 1:
                return person
        
        return -1
