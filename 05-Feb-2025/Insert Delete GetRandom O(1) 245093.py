# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

import random
class RandomizedSet:

    def __init__(self):
        self._map = dict()
        self._list = list()

    def insert(self, val: int) -> bool:
        if val in self._map:
            return False
        self._map[val] = len(self._list)
        self._list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self._map:
            return False
        last_element = self._list[-1]
        idx = self._map[val]
        
        # Swap val with the last element
        self._list[idx] = last_element
        self._map[last_element] = idx  # Update index in map
        
        # Remove val
        self._list.pop()
        del self._map[val]
        return True


    def getRandom(self) -> int:
        idx = random.randint(0, len(self._list) - 1)
        return self._list[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()