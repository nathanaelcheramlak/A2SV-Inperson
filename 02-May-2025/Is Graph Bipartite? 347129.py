# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0] * len(graph) 
        
        def dfs(node, current_color):
            color[node] = current_color
            new_color = 1 if current_color == 2 else 2
            for neighbour in graph[node]:
                if color[neighbour] == current_color:
                    return False
                if color[neighbour] == 0 and not dfs(neighbour, new_color):
                    return False
            return True
        
        for node in range(len(graph)):
            if color[node] == 0 and not dfs(node, 1):
                return False
        return True