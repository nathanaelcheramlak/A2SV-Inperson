# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0
        def backtrack(i, num, squared, path):
            if i == len(squared):
                return sum(map(int, path)) == num
            
            path.append(squared[i])
            x = backtrack(i + 1, num, squared, path)
            path.pop()
            y = False

            if path:
                path[-1] += squared[i]
                y = backtrack(i + 1, num, squared, path)
            return x or y
            
        
        for num in range(1, n + 1):
            squared = num ** 2
            if num % 9 == 0 or num % 9 == 1:
                if backtrack(0, num, str(squared), []):
                    ans += squared
        
        return ans