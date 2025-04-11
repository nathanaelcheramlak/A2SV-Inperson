# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp = {}
        for employee in employees:
            emp[employee.id] = employee

        def dfs(id):
            if not emp[id].subordinates:
                return emp[id].importance

            current = emp[id].importance
            for e in emp[id].subordinates:
                current += dfs(emp[e].id)
            return current
            
        return dfs(id)