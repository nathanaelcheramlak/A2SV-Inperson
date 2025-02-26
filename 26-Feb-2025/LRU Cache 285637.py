# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key=0, val=0):
        self.val, self.key = val, key
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()

        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.prev = self.tail, self.head
    
    # Remove from the list
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # Insert at the head (MRU)
    def insert(self, node):
        prev, nxt = self.tail.prev, self.tail 
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # Remove from the list and delete the LRU from the hashmap
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)