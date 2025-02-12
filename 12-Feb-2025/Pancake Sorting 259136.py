# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(arr, k):
            return arr[k::-1] + arr[k+1:]
        
        i = len(arr) - 1
        ans = list()
        while i > 0:
            max_idx = 0
            for id, val in enumerate(arr[:i+1]):
                if arr[max_idx] <= arr[id]:
                    max_idx = id
            arr = flip(arr, max_idx)
            arr = flip(arr, i)
            ans.extend([max_idx + 1, i + 1])
            i -= 1
        
        return ans




        