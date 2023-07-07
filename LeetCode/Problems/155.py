# NeetCode - Stack
# 155. Min Stack
# Difficulty : Medium
# Algorithm : Stack
# Runtime : 77 ms (45.56%), Memory : 20.1 MB (99.19%)
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min:
            self.min.append(val)
        else:
            if val <= self.min[-1]:
                self.min.append(val)
        return None

    def pop(self) -> None:
        if self.stack.pop() == self.min[-1]:
            self.min.pop()
        return None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
