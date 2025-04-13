# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for start, end, time in times:
            graph[start].append((time, end))

        heap = [(0, k)]
        shortest = {}

        while len(shortest) < n and heap:
            time, currentNode = heappop(heap)
            if currentNode in shortest:
                continue
            shortest[currentNode] = time
            for t, node in graph[currentNode]:
                heappush(heap, (time + t, node))
        
        if len(shortest) < n:
            return -1
        return max(shortest.values())