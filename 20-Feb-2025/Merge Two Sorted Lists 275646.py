# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        merge = ListNode()
        curr = merge

        while l1 or l2:
            if (not l2) or (l1 and l1.val <= l2.val):
                curr.next = ListNode(l1.val)
                curr = curr.next
                l1 = l1.next
            else:
                curr.next = ListNode(l2.val)
                curr = curr.next
                l2 = l2.next

        return merge.next
