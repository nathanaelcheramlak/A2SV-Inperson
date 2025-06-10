# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        permutation = []
        def backtrack(i, path):
            if i == len(s):
                permutation.append("".join(path))
                return
            
            if s[i].isalpha():
                path.append(s[i])
                backtrack(i + 1, path)
                path.pop()

                path.append(s[i].swapcase())
                backtrack(i + 1, path)
                path.pop()
            else:
                path.append(s[i])
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(0, [])
        return permutation

