# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        N = len(equations)
        graph = defaultdict(list)
        nodes = set()
        for i in range(N):
            u, v = equations[i]
            graph[u].append((values[i], v))
            graph[v].append((1 / values[i], u))
            nodes.add(u)
            nodes.add(v)
        
        def dfs(node, target, seen, acc):
            if node == target:
                return True, acc
            seen.add(node)
            for div, v in graph[node]:
                if v not in seen:
                    found, ans = dfs(v, target, seen, acc * div)
                    if found:
                        return True, ans
            
            return False, 1
        
        ans = []
        print(graph)
        for u, v in queries:
            found, val = dfs(u, v, set(), 1)
            if found and u in nodes:
                ans.append(val)
            else:
                ans.append(-1)
        print(graph)
        return ans
