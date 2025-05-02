# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        indegree = [0] * len(graph)
        adj = defaultdict(list)
        for node, path in enumerate(graph):
            indegree[node] += len(path)
            for neighbour in path:
                adj[neighbour].append(node)

        ans = []
        level = list()
        for node in range(len(graph)):
            if indegree[node] == 0:
                level.append(node)
        
        level = deque(level)
        while level:
            node = level.popleft()
            ans.append(node)
            for neighbour in adj[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    level.append(neighbour)

        return sorted(ans)
        
