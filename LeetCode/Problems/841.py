# explore <Queue & Stack> - Conclusion
# 841. Keys and Rooms
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)

        queue = deque()
        queue.append(0)
        visited[0] = True

        while queue:
            x = queue.popleft()
            for room in rooms[x]:
                if not visited[room]:
                    visited[room] = True
                    queue.append(room)

        for v in visited:
            if not v:
                return False
        return True
