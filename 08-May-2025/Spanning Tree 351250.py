# Problem: Spanning Tree - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E

class DSU:
    def __init__(self, size):
        self.parent = [-1 for i in range(size + 1)]
    
    def find(self, node):
        if self.parent[node] < 0:
            return node
        
        visited = []
        while self.parent[node] > 0:
            visited.append(node)
            node =  self.parent[node]
        
        for visited_node in visited:
            self.parent[visited_node] = node
        
        return node

    def union(self, set1, set2):
        p1 = self.find(set1)
        p2 = self.find(set2)

        if p1 == p2:
            return False
        total_nodes = self.parent[p1] + self.parent[p2]
        if self.parent[p1] > self.parent[p2]:
            self.parent[p1] = p2
            self.parent[p2] = total_nodes
        else:
            self.parent[p2] = p1
            self.parent[p1] = total_nodes

        return True

    def connected(self, u, v):
        return self.find(u) == self.find(v)

n, m = map(int, input().split())
dsu = DSU(n)
edges = []
for _ in range(m):
    u, v, weight = map(int, input().split())
    edges.append([weight, u, v])

edges.sort()
weight = 0
for w, u, v in edges:
    if dsu.union(u, v):
        weight += w

print(weight)