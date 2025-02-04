# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        val = ""
        comment = False
        
        for line in source:
            if not comment:
                val = ""  # Reset val for a new line
            i = 0
            while i < len(line):
                if comment:
                    if line[i:i + 2] == "*/":
                        comment = False
                        i += 1  # Skip the closing comment
                else:
                    if line[i:i + 2] == "//":
                        break  # Skip the rest of the line
                    elif line[i:i + 2] == "/*":
                        comment = True
                        i += 1  # Skip the opening comment
                    else:
                        val += line[i]  # Add the character to val
                i += 1
            if not comment and val:
                ans.append(val)  # Add non-empty lines to the answer
        
        return ans