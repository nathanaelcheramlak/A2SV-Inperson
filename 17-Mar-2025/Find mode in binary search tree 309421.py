# Problem: Find mode in binary search tree - https://leetcode.com/problems/find-mode-in-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = defaultdict(int)
        def preorder(node):
            if not node:
                return 
            count[node.val] += 1
            preorder(node.left)
            preorder(node.right)
        preorder(root)

        count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        ans = []
        max_freq = count[0][1]

        for key, value in count:
            if value == max_freq:
                ans.append(key)
        
        return ans