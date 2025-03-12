# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()

    def push(self, x: int) -> None:
        self.stack1.append(x)
        print(self.stack1)

    def pop(self) -> int:
        while self.stack1:
            val = self.stack1.pop()
            self.stack2.append(val)
        value = self.stack2.pop()
        while self.stack2:
            val = self.stack2.pop()
            self.stack1.append(val)
        
        return value

    def peek(self) -> int:
        while self.stack1:
            val = self.stack1.pop()
            self.stack2.append(val)
        if self.stack2:
            value = self.stack2[-1]
        while self.stack2:
            val = self.stack2.pop()
            self.stack1.append(val)
        
        return value or None

    def empty(self) -> bool:
        return not self.stack1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()