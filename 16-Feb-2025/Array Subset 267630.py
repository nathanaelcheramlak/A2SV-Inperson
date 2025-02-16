# Problem: Array Subset - https://practice.geeksforgeeks.org/problems/array-subset-of-another-array2317/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

#User function Template for python3
from collections import Counter

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        dict_a = Counter(a)
        dict_b = Counter(b)
        
        for key, val in dict_b.items():
            if dict_a[key] < val:
                return False
        
        return True