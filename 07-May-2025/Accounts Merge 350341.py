# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class UnionFind:
    def __init__(self):
        self.parent = defaultdict(str)
        self.size = defaultdict(int)
    
    def add_node(self, x):
        self.parent[x] = x
        self.size[x] = 1

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            
        visited = []
        while x != self.parent[x]:
            visited.append(x)
            x = self.parent[x]
        
        for visited_email in visited:
            self.parent[visited_email] = x
        
        return x

    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return
        total_size = self.size[p1] + self.size[p2]
        if self.size[p1] > self.size[p2]:
            self.parent[p2] = p1
            self.size[p1] = total_size
        else:
            self.parent[p1] = p2
            self.size[p2] = total_size

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        get_name = {}
        dsu = UnionFind()

        # Union Nodes
        for account in accounts:
            name, first_email = account[:2]
            for i in range(1, len(account)):
                dsu.union(account[i], first_email)
                get_name[account[i]] = name
        
        # Get Parents
        emails = defaultdict(set)
        for account in accounts:
            for i in range(1, len(account)):
                parent = dsu.find(account[i])
                emails[parent].add(account[i])
        
        # Answer
        ans = []
        for email, much_email in emails.items():
            row = []
            name = get_name[email]
            row.append(name)
            row.extend(sorted(list(much_email)))
            ans.append(row)

        return ans

