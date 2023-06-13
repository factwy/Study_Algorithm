# Conclusion

## P Implement_Queue_using_Stacks.py
```python
class MyQueue:

    def __init__(self):
        self.front = []
        self.back = []
        self.length = 0

    def push(self, x: int) -> None:
        self.front.append(x)
        self.length += 1
        return None

    def pop(self) -> int:
        for _ in range(self.length):
            self.back.append(self.front.pop())
            
        num = self.back.pop()
        self.length -= 1
        
        for _ in range(self.length):
            self.front.append(self.back.pop())
            
        return num

    def peek(self) -> int:
        return self.front[0]

    def empty(self) -> bool:
        if self.front:
            return False
        return True
```

## P Implement_Stack_using_Queues.py
```python
class MyStack:

    def __init__(self):
        self.front = deque()
        self.back = deque()
        self.length = 0

    def push(self, x: int) -> None:
        self.front.append(x)
        self.length += 1
        return None

    def pop(self) -> int:
        self.length -= 1
        for _ in range(self.length):
            self.back.append(self.front.popleft())
        num = self.front[0]
        self.front, self.back = self.back, deque()
        return num

    def top(self) -> int:
        return self.front[-1]

    def empty(self) -> bool:
        if self.front:
            return False
        return True
```

## P Decode_String.py
```python
```

## P Flood_Fill.py
```python
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
        m, n = len(image), len(image[0])
        visited = set([])

        def dfs(x, y):
            nonlocal n, m, image, color
            visited.add((x, y))

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                if (nx, ny) in visited:
                    continue
                if image[x][y] == image[nx][ny]:
                    dfs(nx, ny)
            image[x][y] = color

        dfs(sr, sc)
        return image
```

## P 01_Matrix.py
```python
```

## P Keys_and_Rooms.py
```python
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
```
