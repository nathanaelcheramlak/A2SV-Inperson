# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class UnionFind:
    def __init__(self):
        self.parent = {}
    
    def find(self, v):
        if v not in self.parent:
            self.parent[v] = v
            return v
        
        visited = []
        while self.parent[v] != v:
            visited.append(v)
            v = self.parent[v]

        for node in visited:
            self.parent[node] = v
        return v
    
    def union(self, u, v):
        p1, p2 = self.find(u), self.find(v)
        if p1 == p2:
            return
        
        if p1 < p2:
            self.parent[p2] = p1
        else:
            self.parent[p1] = p2

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        N = len(s1)
        unionFind = UnionFind()
        for i in range(N):
            unionFind.union(s1[i], s2[i])
        
        ans = []
        for i in range(len(baseStr)):
            ans.append(unionFind.find(baseStr[i]))
        
        return ''.join(ans)
