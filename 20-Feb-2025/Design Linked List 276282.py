# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.dummy = Node()
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        
        temp = self.dummy.next
        for _ in range(index):
            temp = temp.next
        
        return temp.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.dummy.next
        self.dummy.next = new_node
        self.length += 1

        if not self.tail:
            self.tail = self.dummy.next        

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.dummy.next:
            self.tail.next = new_node
            self.tail = self.tail.next
            self.length += 1
        else:
            self.addAtHead(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return

        new_node = ListNode(val)
        if index == self.length:
            self.addAtTail(val)
            return

        temp = self.dummy
        for _ in range(index):
            temp = temp.next

        new_node.next = temp.next  
        temp.next = new_node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        
        temp = self.dummy
        for _ in range(index):
            temp = temp.next
        
        if temp.next == self.tail:
            self.tail = temp
        temp.next = temp.next.next
        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)