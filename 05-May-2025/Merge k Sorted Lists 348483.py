# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        arr = []
        for lst in lists:
            while lst:
                arr.append(lst.val)
                lst = lst.next
        arr.sort()
        dummy = ListNode()
        curr = dummy
        print(arr)
        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next

        