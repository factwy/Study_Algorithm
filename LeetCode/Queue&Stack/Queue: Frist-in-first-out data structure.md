# Queue: First-in-first-out Data Structure

## A First-in-first-out data structure
- first element added to the queue will be processed first
- the new element is always added at the end of queue (enqueue)
- remove the first element (dequeue)

## A Queue - Implementation
- need to implement queue : dynamic array and index pointing to the head of the queue
- queue support two operations : enqueue, dequeue
- implemented queue : straightforward and inefficient
- drawback : with the movement of the start pointer, more and more space is wasted and it will be unacceptable when we only have a space limit

## A Circular Queue
- need to implement queue : fixed-size array and two pointers to indicate the starting position and the ending position
- goal : reuse the wasted storage

## P Implement Circular Queue
- need to implement circular queue class
  1. MycircularQueue(k) : initializes the object with the size of the queue to be k
  2. Front() : gets the front item from the circular queue
  3. Rear() : gets the last item from the circular queue
  4. enQueue(int value) : inserts an element into the circular queue
  5. deQueue() : deletes an element from the circular queue
  6. isEmpty() : checks whether the circular queue is empty or not
  7. isFull() : checks whether the circular queue is full or not

```python
class MyCircularQueue:

    def __init__(self, k: int):
        # initializes the object with the size of queue to be k
        self.queue = [-1] * k
        self.size = k
        self.start , self.end = 0, -1

    def enQueue(self, value: int):
        # inserts an element into the circular queue
        if self.isFull():
            return False
        self.end = (self.end + 1) % self.size
        self.queue[self.end] = value
        return True
        

    def deQueue(self):
        # deletes an element from the circular queue
        if self.isEmpty():
            return False
        self.queue[self.start] = -1
        self.start = (self.start + 1) % self.size
        return True
        

    def Front(self):
        # gets the front item from the circular queue
        if self.isEmpty():
            return -1
        return self.queue[self.start]

    def Rear(self):
        # gets the last item from the circular queue
        if self.isEmpty():
            return -1
        return self.queue[self.end]

    def isEmpty(self):
        # checks whether the circular queue is empty or not
        if self.queue[self.end] == -1:
            return True
        return False

    def isFull(self):
        if self.queue[(self.end + 1) % self.size] != -1:
            return True
        return False
```

<br>

[Queue & Stack](https://leetcode.com/explore/learn/card/queue-stack/228/first-in-first-out-data-structure/)
