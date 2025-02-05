# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        ans = list()

        for word in words:
            current_row = set(word.lower())
            if current_row <= row1 or current_row <= row2 or current_row <= row3:
                ans.append(word)
        
        return ans