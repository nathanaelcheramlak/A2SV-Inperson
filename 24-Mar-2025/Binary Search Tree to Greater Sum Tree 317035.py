# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, s):
            if not node:
                return s
            right = dfs(node.right, s)  
            node.val += right  
            return dfs(node.left, node.val) 
            
        dfs(root, 0)
        return root