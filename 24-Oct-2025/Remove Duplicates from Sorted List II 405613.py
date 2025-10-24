# Problem: Remove Duplicates from Sorted List II - https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        counter = defaultdict(int)
        temp = head
        while temp:
            counter[temp.val] += 1
            temp = temp.next
        
        dummy = ListNode()
        temp = dummy
        while head:
            if counter[head.val] == 1:
                temp.next = head
                temp = temp.next
            head = head.next
        
        temp.next = None
        return dummy.next

            