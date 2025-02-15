# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = self.sortArray(arr[:mid])
        right_half = self.sortArray(arr[mid:])

        i = j = 0
        merged = []

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                merged.append(left_half[i])
                i += 1
            else:
                merged.append(right_half[j])
                j += 1

        merged.extend(left_half[i:])
        merged.extend(right_half[j:])

        return merged