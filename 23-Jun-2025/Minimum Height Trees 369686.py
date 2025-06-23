# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0] * n
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        
        nodes = set([i for i in range(n)])
        leaves = []
        for node, ind in enumerate(indegree):
            if ind == 1: # Leaf
                leaves.append(node)
        
        while len(nodes) > 2:
            new_leaves = []
            for node in leaves:
                nodes.discard(node)
                for nei in adj[node]:
                    indegree[nei] -= 1
                    if indegree[nei] <= 1 and nei in nodes:
                        new_leaves.append(nei)
            leaves = new_leaves
        
        return list(nodes)
