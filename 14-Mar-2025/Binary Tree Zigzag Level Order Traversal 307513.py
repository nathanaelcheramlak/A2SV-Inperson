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
        ans = [[root.val]]
        direction = 0
        while level:
            new_level = []
            for node in level:
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)

            values = []
            for node in new_level:
                values.append(node.val)

            if not values:
                break

            if direction == 0:
                ans.append(values[::-1])
            else:
                ans.append(values)
            level = new_level
            direction = 0 if direction == 1 else 1
        
        return ans