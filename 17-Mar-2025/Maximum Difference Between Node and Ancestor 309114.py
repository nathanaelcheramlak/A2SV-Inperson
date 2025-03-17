# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root, minimum, maximum, curr_max = 0):
            if not root:
                return curr_max
            minimum = min(minimum, root.val)
            maximum = max(maximum, root.val)
            curr_max = max(curr_max, maximum - minimum)

            return max(dfs(root.left, minimum, maximum, curr_max), 
                        dfs(root.right, minimum, maximum, curr_max))

        return dfs(root, root.val, root.val)