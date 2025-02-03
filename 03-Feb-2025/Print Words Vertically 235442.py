# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(' ')
        maxLen = max(len(word) for word in words)
        ans = list()
        p = 0

        while p < maxLen:
            val = []
            for i in range(len(words)):
                if p < len(words[i]):
                    val.append(words[i][p])
                else:
                    val.append(' ')
            for i in range(len(val) -1, -1, -1):
                if val[i] == ' ':
                    val.pop()
                else:
                    break
                    
            ans.append(''.join(val))
            p += 1
    
        return ans