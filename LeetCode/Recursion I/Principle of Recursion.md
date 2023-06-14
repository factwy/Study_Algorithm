# Principle of Recursion

## A Principle of Recursion
- A recursive function should have the following properties so that it does not result in an infinite loop
  1. A simple **base case** (or cases) - a terminating scenario that does not use recursion to produce an answer.
  2. A set of rules, also known as **recurrence relation** that reduces all other cases towards the base case.

## P Reverse_String.py
```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s_len = len(s)
        visited = [False] * s_len
        
        def recursion(index, arr):
            nonlocal visited, s_len
            if index >= s_len or not arr:
                return
            if visited[index]:
                return
            
            visited[index], visited[s_len-index-1] = True, True
            recursion(index+1, arr)
            arr[index], arr[s_len-index-1] = arr[s_len-index-1], arr[index]
            
        recursion(0, s)
```
- This implement is too big complexity, so need to implement with another algorithms like "Two Pointers"

## A Recursion Function
- GuideLines to implement recursion functions
  1. Break the problem down into smaller scopes, such as x0∈X, x1∈X, ... , xn∈X
  2. call function F(x0), F(x1), ..., F(xn) recursively to solve the subproblems of X
  3. Finally, process the results from the recursive function calls to solve the problem corresponding to X
 
## P Swap_Nodes_in_Pairs.py
```python
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def swap(self, node):
            if not node:
                return
            if not node.next:
                return
            
            node.val, node.next.val = node.next.val, node.val
            swap(self, node.next.next)
            
        swap(self, head)
        return head
```
