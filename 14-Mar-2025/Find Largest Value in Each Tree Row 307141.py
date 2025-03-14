# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        level = [root]
        ans = []
        while level:
            new_level = []
            curr_max = float('-inf')
            for node in level:
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
                
                curr_max = max(curr_max, node.val)
            ans.append(curr_max)
            level = new_level
        
        return ans