# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def backtrack(i, path):
            if i == len(s):
                if len(path) == 4 and all(int(octet) <= 255 for octet in path) and all(octet[0] != '0' or len(octet) == 1 for octet in path):
                    ans.append('.'.join(path))
                
                return

            if 12 - 3 * len(path) < (len(s) - 1) - (i + 1):
                return
            
            path.append(s[i])
            backtrack(i + 1, path)
            path.pop()
            
            if path:
                path[-1] += s[i]
                backtrack(i + 1, path)
            
        
        backtrack(0, [])
        return ans