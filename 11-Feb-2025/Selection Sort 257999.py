# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution: 
    def selectionSort(self, arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            
            if min_idx != i: # swap
                arr[min_idx], arr[i] = arr[i], arr[min_idx]
        return arr