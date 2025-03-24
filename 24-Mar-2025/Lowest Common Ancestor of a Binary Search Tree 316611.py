# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return
            left = min(p.val, q.val)
            right = max(p.val, q.val)
            if left <= node.val <= right:
                return node
            l = r = None
            if node.val > left:
                l = dfs(node.left)
            else:
                r = dfs(node.right)

            if l:
                return l
            return r
        
        return dfs(root)
            