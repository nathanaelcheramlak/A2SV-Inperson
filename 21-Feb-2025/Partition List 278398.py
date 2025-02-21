# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small_dummy = ListNode()
        small = small_dummy
        big_dummy = ListNode()
        big = big_dummy

        current_node = head
        while current_node:
            if current_node.val < x:
                small.next = current_node
                small = small.next
            else:
                big.next = current_node
                big = big.next
            current_node = current_node.next
        
        big.next = None
        small.next = big_dummy.next
        return small_dummy.next