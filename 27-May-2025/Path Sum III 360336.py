# Problem: Path Sum III - https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, curr_sum, prefix):
            if not node:
                return 0
            curr_sum += node.val
            count = 0
            if curr_sum - targetSum in prefix:
                count += prefix[curr_sum - targetSum]
                
            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
            count += dfs(node.left, curr_sum, prefix) + dfs(node.right, curr_sum, prefix)
            prefix[curr_sum] -= 1

            return count
        
        return dfs(root, 0, {0: 1})