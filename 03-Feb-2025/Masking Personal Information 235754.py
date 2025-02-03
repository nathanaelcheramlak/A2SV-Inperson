# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:

        if '@' not in s:
            middle = '***-***-'
            lastDigits = []
            for digit in s:
                if digit.isdigit():
                    lastDigits.append(digit)
            print(lastDigits)
            if len(lastDigits) == 10:
                return middle + ''.join(lastDigits[-4:])
            else:
                first = '+' + '*' * (len(lastDigits) - 10) + '-'
                return first + middle + ''.join(lastDigits[-4:])
        else:
            at = s.find('@')
            return s[0].lower() + '*****' + s[at - 1].lower() + s[at] + s[at + 1:].lower()