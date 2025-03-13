# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # level = [1,1 ]
        n = rowIndex
        if rowIndex == 0:
            return [1]
        # n-=1
        # while n > 0:
        #     nextLevel = [1]
        #     for i in range(len(level)-1):
        #         nextLevel.append(level[i] + level[i + 1])
        #     nextLevel.append(1)
        #     level = nextLevel
        #     n-=1
        # return level
        ans = []
        def dfs(level , n):
            nonlocal ans
            if n == 0:
                ans = level[:]
                return
            nextLevel = [1]
            for i in range(len(level)-1):
                nextLevel.append(level[i] + level[i + 1])
            nextLevel.append(1)
            dfs(nextLevel , n-1)
        dfs([1,1] , n-1)
        return ans

