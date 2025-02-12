# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Bubble Sort
        n = len(heights)
        for i in range(n):
            for j in range(n - i - 1):
                if heights[j + 1] > heights[j]:
                    heights[j + 1], heights[j] = heights[j], heights[j + 1]
                    names[j + 1], names[j] = names[j], names[j + 1]

        return names