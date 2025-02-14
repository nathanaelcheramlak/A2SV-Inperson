# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        n = len(s2)
        count = Counter(s1)
        window = Counter(s2[:k])
        if count == window:
            return True
        
        for left in range(1, n - k + 1):
            # Update Window
            window[s2[left - 1]] -= 1
            if window[s2[left - 1]] == 0:
                del window[s2[left - 1]]
            window[s2[left + k - 1]] += 1

            if window == count:
                return True
        
        return False