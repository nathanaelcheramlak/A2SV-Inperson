# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        N = len(quiet)
        dic = dict([val, idx] for idx, val in enumerate(quiet))
        print(dic)
        for a, b in richer:
            graph[b].append(a)
        
        cache = dict()
        def dfs(node):
            if not graph[node]:
                return quiet[node]
            if node in cache:
                return cache[node]
            minimum = quiet[node]
            for neighbour in graph[node]:
                minimum = min(minimum, dfs(neighbour))
            cache[node] = minimum
            return minimum
        
        answer = []
        for node in range(N):
            answer.append(dic[dfs(node)])
        return answer