# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

from collections import defaultdict
    
import sys
import threading

input_fn = lambda: sys.stdin.readline().strip()

def main():
    def solve():
        n, m = map(int, input().split())

        graph = defaultdict(list)
        for _ in range(m):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)
            if (len(graph[a]) == n - 1 or len(graph[b]) == n - 1) and m == n - 1:
                return "star topology"
            
        for nei in graph.values():
            if len(nei) > 2:
                return "unknown topology"
            
        visited = set()
        def is_cycle(node, parent):
            visited.add(node)
            for nei in graph[node]:
                if nei in visited:
                    if nei != parent:
                        return True
                elif nei not in visited:
                    if is_cycle(nei, node):
                        return True 
            return False

        if is_cycle(1, -1):
            return "ring topology"
        else:
            return "bus topology"

    print(solve())

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
