# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        level = [root]
        ans = []
        values = [root.val]
        direction = 0

        while level:
            if direction == 1:
                ans.append(values[::-1])
            else:
                ans.append(values)

            values = []
            new_level = []
            for node in level:
                if node.left:
                    new_level.append(node.left)
                    values.append(node.left.val)
                if node.right:
                    new_level.append(node.right)
                    values.append(node.right.val)

            level = new_level
            direction = 0 if direction == 1 else 1
        
        return ans