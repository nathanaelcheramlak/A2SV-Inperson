# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_sum = 0
        length = 0

        current = head
        while current:
            length += 1
            current = current.next
        
        mid = head
        for _ in range(length // 2 - 1):
            mid = mid.next
        
        # Reverse the right half
        last_node = None
        while mid:
            next_node = mid.next
            mid.next = last_node
            last_node = mid
            if not next_node:
                break
            mid = next_node
        
        for _ in range(length // 2):
            max_sum = max(max_sum, head.val + mid.val)
            head = head.next
            mid = mid.next
        
        return max_sum