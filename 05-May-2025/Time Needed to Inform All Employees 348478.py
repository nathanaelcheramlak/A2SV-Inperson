# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for employee, m in enumerate(manager):
            graph[m].append(employee)
        
        max_time = float('-inf')
        def dfs(node, time):
            nonlocal max_time
            max_time = max(max_time, time)

            for neighbour in graph[node]:
                dfs(neighbour, time + informTime[node])
        
        dfs(headID, 0)
        return max_time
        