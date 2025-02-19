# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            head = ListNode(0, head)
            dummy = head
            for _ in range(n):
                dummy = dummy.next
            
            temp = head
            while dummy.next:
                dummy = dummy.next
                temp = temp.next
            
            temp.next = temp.next.next
            return head.next