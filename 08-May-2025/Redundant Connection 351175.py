# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = defaultdict(int)
    
    def find(self, v):
        if v not in self.parent:
            self.parent[v] = v

        visited = []
        while self.parent[v] != v:
            visited.append(v)
            v = self.parent[v]
        
        for visited_node in visited:
            self.parent[visited_node] = v
        
        return v

    def union(self, u, v):
        p1, p2 = self.find(u), self.find(v)
        if p1 == p2:
            return False
        
        if self.size[p1] < self.size[p2]:
            self.parent[p1] = p2
            self.size[p2] += self.size[p1]
        else:
            self.parent[p2] = p1
            self.size[p1] += self.size[p2]
        
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        unionFind = UnionFind()
        for u, v in edges:
            if not unionFind.union(u, v):
                return [u, v]