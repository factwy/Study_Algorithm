# Recurrenece Relation

## A Recurrence Relation
- recurrence relation : the relationship between the result of a problem and the result of its subproblems.
- base case : the case where one can compute the answer directly without any further recursion calls

  Once we figure out the above two elements, to implement a recursive function we simply call the function itself according to the **recurrence relation** until we reach the **base case**.

## P Reverse_Linked_List.py
```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        answer = ListNode(head.val, None)
        
        def recursion(self, node):
            nonlocal answer
            if node.next:
                answer = ListNode(node.next.val, answer)
                recursion(self, node.next)
        
        recursion(self, head)
        return answer
```

## P Search_in_a_Binary_Search_Tree.py
```python
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        
        while node.val != val:
            if node.val > val:
                node = node.left
            else:
                node = node.right
            if not node:
                break
                    
        return node
```

## P Pascal's_Triangle_II.py
```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        answer = [[-1] * (rowIndex+1) for _ in range(rowIndex+1)]
        
        
        def recursion(self, x, y):
            nonlocal answer
            if y == 0 or y == x:
                answer[x][y] = 1
                return
            
            if answer[x-1][y] == -1:
                recursion(self, x-1, y)
            if answer[x-1][y-1] == -1:
                recursion(self, x-1, y-1)
                
            answer[x][y] = answer[x-1][y] + answer[x-1][y-1]
            
            
        for i in range(rowIndex+1):
            recursion(self, rowIndex, i)
            
        return answer[rowIndex]
```
