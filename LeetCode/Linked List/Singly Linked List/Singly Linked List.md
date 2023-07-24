# Introduction - Singly Linked List

- Linked List in  Python

If we want to get the ith element, It takes us O(N) time on average to visit and element by index, where N is the length of the linked list

```python
class ListNode:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next
```

# Add Operation - Singly Linked List

- If we want to add a new value after a given node **prev**, we should
1. Initialize a new node **cur** with the given value
2. Link the "next" field of **cur** to prev's next node **next**
3. Link the "next' field in **prev** to **cur**

You can insert a new noew into a linked list in O(1) time complexity

# Delete Operation - Singly Linked List

- If we want to delete an existing node **cur** from the singly linked list
1. Find cur's previous node **prev** and its next node **next**
2. Link **prev** to cur's next node **next**

We have to traverse the linked list from the head node to find out **prev** which will take O(N) time on average

The Space complexity is O(1) because we only need constant space to store our pointers
