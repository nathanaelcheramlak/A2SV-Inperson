# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def path(currSum , node):
            if not node:
                return 0

            if not node.left and not node.right:
                return currSum * 10  + node.val
                
            res = 0
            res += path(currSum * 10 + node.val , node.left)
            res += path(currSum * 10 + node.val , node.right)
            return res
        return path(0 , root)
        
