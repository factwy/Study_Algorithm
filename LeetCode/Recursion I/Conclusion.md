 # Conclusion
 - General workflow to solve a recursion problem
  1. Define the **recursion function**
  2. Write down the **recurrence relation** and **base case**
  3. Use **memoization** to eliminate the **duplicate calculation** problem, if it exits.
  4. Whenever possible, implement the functions as **tail recursion**, to optimize the space complexity

## A Conclusion - Recursion I
- When in doubt, write down the **recurrence relationship.**
- whenever possible, apply **memoization**
- when stack overflows, **tail recursion** might come to help

## P Merge_Two_Sorted_Lists
```python
# 21. Merge Two Sorted Lists
# difficulty : Easy
# algorithm : Recursion
# Runtime : 61 ms (11.34%), Memory : 16.6 MB (11.39%)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        def merge(self, list1, list2):
            now = ListNode()
            # base case
            if list1 == list2 == None:
                return None
            
            # recurrence relation
            if list1 == None:
                now.val = list2.val
                now.next = merge(self, list1, list2.next)
            elif list2 == None:
                now.val = list1.val
                now.next = merge(self, list1.next, list2)
            elif list1.val < list2.val:
                now.val = list1.val
                now.next = merge(self, list1.next, list2)
            else:
                now.val = list2.val
                now.next = merge(self, list1, list2.next)
                
            return now
                
        
        return merge(self, list1, list2)
```
