# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        k = len(p)
        ans = list()
        window = Counter((s[:k]))
        count = Counter(p)
        if window == count:
            ans.append(0)
        
        for left in range(1, n - k + 1):
            # update window
            window[s[left - 1]] -= 1
            window[s[left + k - 1]] += 1
            if window[s[left - 1]] == 0:
                del window[s[left - 1]]

            if window == count:
                ans.append(left)
        
        return ans