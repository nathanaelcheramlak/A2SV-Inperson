# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        inorder(root)
        
        def dfs(arr):
            if not arr:
                return None
            mid = len(arr) // 2
            node = TreeNode(arr[mid]) 
            node.left = dfs(arr[:mid])
            node.right = dfs(arr[mid + 1:])

            return node
        
        return dfs(arr)