# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        n = len(nums)
        root = TreeNode(nums[n // 2])
        root.right = self.sortedArrayToBST(nums[n // 2 + 1:])
        root.left = self.sortedArrayToBST(nums[:n // 2])

        return root


