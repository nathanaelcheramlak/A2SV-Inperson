# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        map = dict()
        for domain in cpdomains:
            count, dom = domain.split()
            sub = dom.split('.')
            for i in range(len(sub) - 1, -1, -1):
                d = '.'.join(sub[i:])
                map[d] = map.get(d, 0) + int(count)
        
        ans = []
        for key, value in map.items():
            ans.extend([str(value) + " " + key])
        
        return ans