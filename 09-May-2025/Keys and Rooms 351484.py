# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # BFS
        visited = set([0])
        level = deque(rooms[0])
        while level and len(visited) < len(rooms):
            rid = level.popleft()
            visited.add(rid)
            for key in rooms[rid]:
                if key not in visited:
                    level.append(key)
        
        if len(visited) == len(rooms):
            return True
        return False
