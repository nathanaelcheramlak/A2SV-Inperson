# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node.left and not node.right:
                ans += 1
                return (node.val, 1)
            total = node.val
            count = 1
            if node.left:
                s, c = dfs(node.left)
                total += s
                count += c
            if node.right:
                s, c = dfs(node.right)
                total += s
                count += c

            if total // count == node.val:
                ans += 1
            return (total, count)
        dfs(root)
        return ans