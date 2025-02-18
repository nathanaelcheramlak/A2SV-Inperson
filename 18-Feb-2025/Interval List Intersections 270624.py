# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        one = 0 # Iterate over the first list
        two = 0 # Iterate over the second list
        ans = list()

        while one < len(firstList) and two < len(secondList):
            start = max(firstList[one][0], secondList[two][0])
            end = min(firstList[one][1], secondList[two][1])

            if start <= end:
                ans.append([start, end])
            if firstList[one][1] < secondList[two][1]:
                one += 1
            else: 
                two += 1

        return ans