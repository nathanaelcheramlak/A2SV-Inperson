# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        ans = []

        for num in arr2:
            if num in count:
                ans.extend([num] * count[num])
                del count[num]

        for num in sorted(count.keys()):
            ans.extend([num] * count[num])

        return ans