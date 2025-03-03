# Problem: Design Browser History - https://leetcode.com/problems/design-browser-history/description/

class ListNode:

    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = ListNode(homepage)

    def visit(self, url: str) -> None:
        Node = ListNode(url)
        self.current.next = Node
        Node.prev = self.current
        self.current = self.current.next

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if not self.current.prev:
                return self.current.url
            self.current = self.current.prev
        return self.current.url

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if not self.current.next:
                return self.current.url
            self.current = self.current.next
        return self.current.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)