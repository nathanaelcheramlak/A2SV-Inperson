# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = list()
        dummy = ListNode()
        temp = dummy        

        current_node = head
        while current_node:
            stack.append(current_node.val)
            current_node = current_node.next
        
        while stack:
            val = stack.pop()
            new_node = ListNode(val)
            temp.next = new_node
            temp = temp.next
        
        return dummy.next

