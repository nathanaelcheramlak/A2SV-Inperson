# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

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
    def equationsPossible(self, equations: List[str]) -> bool:
        dsu = UnionFind()
        for equation in equations:
            if equation[1] == '=':
                dsu.union(equation[0], equation[3])
        
        for equation in equations:
            if equation[1] == '!':
                if dsu.find(equation[0]) == dsu.find(equation[3]):
                    return False
        
        return True