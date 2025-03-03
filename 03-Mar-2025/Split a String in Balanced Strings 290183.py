# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balanced_count = 0
        balance = 0
        count = 0
        for letter in s:
            count += 1
            if letter == 'R':
                balance += 1
            else:
                balance -= 1

            if count and balance == 0:
                balanced_count += 1
                count = 0
                balance = 0
        
        return balanced_count

            