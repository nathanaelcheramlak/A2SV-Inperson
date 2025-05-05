# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0] * n
        for a, b in edges:
            indegree[b] += 1
        
        zero_count = 0
        zero = 0
        for idx, node in enumerate(indegree):
            if node == 0:
                zero = idx
                zero_count += 1
        if zero_count == 1:
            return zero
        return -1