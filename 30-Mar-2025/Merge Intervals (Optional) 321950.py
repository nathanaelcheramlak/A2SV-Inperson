# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []

        start = intervals[0][0]
        end = intervals[0][1]

        for s, e in intervals:
            if s > end:
                ans.append([start, end])
                start = s
            end = max(e, end)

        ans.append([start, end])
        return ans