# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        mp = dict()
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] < nums2[i]:
                stack.pop()
            if len(stack) == 0:
                mp[nums2[i]] = -1
            else:
                mp[nums2[i]] = stack[-1]
            stack.append(nums2[i])
            
        ans = []
        for num in nums1:
            ans.append(mp[num])
        return ans