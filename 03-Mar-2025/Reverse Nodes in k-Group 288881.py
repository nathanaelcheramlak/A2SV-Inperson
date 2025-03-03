# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         val = val
#         next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        current = head

        length = 0
        while current:
            length += 1
            current = current.next

        current = head
        for i in range(length // k):
            stack = list()
            for _ in range(k):
                stack.append(current)
                current = current.next
            while stack:
                temp.next = stack.pop()
                temp = temp.next
        temp.next = current
        return dummy.next