# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        while head:
            if head.val != val:
                temp.next = head
                temp = temp.next
            else:
                temp.next = None
            head = head.next
        
        return dummy.next