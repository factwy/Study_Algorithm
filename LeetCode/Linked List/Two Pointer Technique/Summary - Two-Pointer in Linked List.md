# Summary - Two-Pointer in Linked List

## Tips
**1. Always examine if the node is null before you call the next field.**
**2. Carefully define the end conditions of your loop.**

## Complexity Analysis
- space complexity : If you use pointers without any other extra space, the space complexity will be O(1)
- time complexity : We need to analyze **how many times we will run our loop**

  1. If there is no cycle, the fast pointer takes N/2 times to reach the end of the linked list, where N is the length of the linked list.
  2. If there is cycle, the fast pointer needs M times to catch up the slower pointer, where M is the length of the cycle in the list.

  So, the time complexity of this algorithm is O(N)
