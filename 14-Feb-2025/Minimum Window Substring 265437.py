# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_subset(smaller, larger):
            return all(item in larger and larger[item] >= smaller[item] for item in smaller)
        count = Counter(t)
        curr = defaultdict(int)
        ans = [float('-inf'), float('inf')]
        left = 0

        for right, char in enumerate(s):
            curr[char] += 1
            while is_subset(count, curr):
                if ans[1] - ans[0] > right - left:
                    ans = [left, right]
                curr[s[left]] -= 1
                if curr[s[left]] <= 0:
                    del curr[s[left]]
                left += 1
        
        if ans == [float('-inf'), float('inf')]:
            return ''
        return s[ans[0]: ans[1] + 1]
            