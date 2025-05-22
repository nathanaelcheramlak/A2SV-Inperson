# Problem: The Unique Topological Sort - https://basecamp.eolymp.com/en/problems/10652

from collections import defaultdict, deque
def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    indegree = [0] * (n + 1)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    level = deque()
    for node, indeg in enumerate(indegree[1:]):
        if indeg == 0:
            level.append(node + 1)
    # print(graph, level)
    order = []
    unique = True
    while level:
        for _ in range(len(level)):
            node = level.popleft()
            order.append(node)
            # print(node, indegree)
            for nei in graph[node]:
                indegree[nei] -= 1
                # print(node, '->', nei, indegree)
                if indegree[nei] == 0:
                    level.append(nei)
        
        # print(level)
        if len(level) > 1:
            unique = False
            break
        
    # print(order)
    if not unique:
        return 'NO'
    if len(order) != n:
        return -1
    for i in range(len(order) - 1):
        curr, prev = order[i + 1], order[i]
        if curr not in graph[prev]:
            return -1
    return 'YES'

print(main())