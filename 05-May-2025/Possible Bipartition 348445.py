# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        color = [0] * (n + 1)
        def dfs(node, curr_color):
            color[node] = curr_color
            new_color = 1 if curr_color == 2 else 2
            for neighbour in graph[node]:
                if color[neighbour] != 0 and color[neighbour] != new_color:
                    return False
                if color[neighbour] == 0 and not dfs(neighbour, new_color):
                    return False
            
            return True

        for node in range(1, n + 1):
            if color[node] == 0:
                if not dfs(node, 1):
                    return False
        
        return True