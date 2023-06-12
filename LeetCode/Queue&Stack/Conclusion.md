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
