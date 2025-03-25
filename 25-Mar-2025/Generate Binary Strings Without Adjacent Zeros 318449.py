# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        def backtrack(path):
            if len(path) == n:
                ans.append(''.join(path))
                return

            path.append('1')
            backtrack(path)
            path.pop()

            if (path and path[-1] != '0') or not path:
                path.append('0')
                backtrack(path)
                path.pop()   

        backtrack([])
        return ans
