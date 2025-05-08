# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1] * size
    
    def find(self, v):
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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        def find_distance(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)
        
        heap = []
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                distance = find_distance(x1, y1, x2, y2)
                heappush(heap, [distance, i, j])
        
        unionFind = UnionFind(N)
        weight = 0
        edge_count = 0
        while edge_count < N - 1:
            distance, p1, p2 = heappop(heap)
            if unionFind.union(p1, p2):
                weight += distance
                edge_count += 1
        
        return weight