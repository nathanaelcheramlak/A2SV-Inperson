# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        left = 0
        right = 0
        answer = list()
        while right < len(s):
            # Find the last occurrence of current character
            right = len(s) - 1 - s[::-1].index(s[left])
            
            i = left + 1
            while i < right:
                # Find the last occurrence of each character in current partition
                last_pos = len(s) - 1 - s[::-1].index(s[i])
                right = max(right, last_pos)
                i += 1
                
            answer.append(right - left + 1)  # Store partition length
            left = right + 1
            right = left  # Reset right to new left position
        
        return answer