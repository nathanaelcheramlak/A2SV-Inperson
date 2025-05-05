# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        def merge_sort(node):
            if not node.next:
                return node
            
            left_part, right_part = divide(node)
            left = merge_sort(left_part)
            right = merge_sort(right_part)

            return merge(left, right)

        
        def divide(head):
            slow = head
            fast = head
            while fast and fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            right = slow.next
            left = head
            slow.next = None

            return left, right
        
        def merge(left, right):
            dummy = ListNode()
            curr = dummy
            while left and right:
                if left.val < right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next
            if left:
                curr.next = left
            if right:
                curr.next = right

            return dummy.next

        return merge_sort(head)            
