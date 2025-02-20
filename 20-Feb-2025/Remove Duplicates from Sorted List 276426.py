# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        current_node = head
        prev_val = ListNode(1000)
        while current_node:
            if current_node.val == prev_val.val:
                prev_val.next = current_node.next 
                current_node = current_node.next
                continue
                
            prev_val = current_node
            current_node = current_node.next

        return head