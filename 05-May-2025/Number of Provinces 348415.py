# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class UnionFind:
    def __init__(self, size):
        self.parent = [-1] * size
    
    def find(self, node):
        visited = []
        while self.parent[node] >= 0:
            visited.append(node)
            node = self.parent[node]
        
        for v in visited:
            self.parent[v] = node
        return node

    def union(self, x, y):
        parx, pary = self.find(x), self.find(y)
        if parx == pary:
            return
        
        total_node = self.parent[parx] + self.parent[pary]
        if self.parent[parx] < self.parent[pary]:
            self.parent[parx] = total_node
            self.parent[pary] = parx
        else:
            self.parent[parx] = pary
            self.parent[pary] = total_node
    
    def get_parents(self):
        return self.parent

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        dsu = UnionFind(N)
        for i in range(N):
            for j in range(i + 1):
                if i != j and isConnected[i][j] == 1:
                    dsu.union(i, j)

        arr = dsu.get_parents()
        return sum(1 for node in arr if node < 0)
