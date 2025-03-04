# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrow = 0

        i = 0
        while i < len(points):
            start, end = points[i]
            while points[i][0] <= end:
                i += 1
                if i == len(points):
                    return arrow + 1
                end = min(end, points[i][1])
                
            arrow += 1
            print(i, arrow)
        return arrow