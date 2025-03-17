# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, node: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not node:
            return TreeNode(val)
        if node.val > val:
            node.left = self.insertIntoBST(node.left, val)
            return node

        node.right = self.insertIntoBST(node.right, val)
        return node

            