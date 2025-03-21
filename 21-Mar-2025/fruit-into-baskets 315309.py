# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = defaultdict(int)
        left = 0
        max_len = 0
        for right in range(len(fruits)):
            window[fruits[right]] += 1
            while len(window) > 2:
                window[fruits[left]] -= 1
                if window[fruits[left]] == 0:
                    del window[fruits[left]] 
                left += 1
            max_len = max(max_len, right - left + 1)

        return max_len