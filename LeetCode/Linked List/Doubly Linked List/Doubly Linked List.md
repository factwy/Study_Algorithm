# Doubly Linked List

## Definition
- The doubly linked list works in a similar way but has one more reference field which is known as the "prev" field.

```python
class DoublyListNode:
  def __init__(self, val=0, next=None, prev=None):
    self.val = val
    self.next = next
    self.prev = prev
```

- We can access data in the same exact way as in a singly linked list.
  1. We are not able to access a random position in constant time.
  2. We have to traverse from the head to get the i-th node we want.
  3. The time complexity in the worse case will be O(N), where N is the length of the linked list.
 
## Add Operation
1. Link cur with prev and next, where next is the original next node of prev
2. re-link the prev and next with cur

## Delete Operation
- Unlike the sinlgy linked list, it is easy to get the previous node in constant time with the "prev" field.

- What if we want to delete the first node or the last node?
  1. first node
      ```python
      head = head.next
      head.prev = None
      return head
      ```
  2. last node
     ```python
     cur = head
     while cur.next:
       cur = cur.next
     cur = None
     return head
     ```
