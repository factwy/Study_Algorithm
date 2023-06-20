# Complexity Analysis

## A Time Complexity - Recursion
- Given a recursion algorithm, its time complexity O(T) is typically the produce of **the number of recursion invocations(R)** and **the time complexity of calculation(O(s))** that incurs along with each recursion call
- O(T) = R * O(s)
- Memoization not ony optimizes the time complexity of algorithm, but also simplifies the calculation of time complexity

## A Space Complexity - Recursion
- two parts of the space consumption that one should bear in mind when calculating the space complexity of a recursion algorithm
- **recursion related** and **non-recursion related space**

## A Tail Recursion
- **Tail recursion** is a recursion where the recursive call is the final instruction in the recursion function.
- And there should be only **one** recursive call in the function
- The benefit of having tail recursion is that it could **avoid the accumulation of stack overheads** during the recursive calls, since the system could **reuse a fixed amount space** in the stack for each recursive call.

## P Maximum_Depth_of_Binary_Tree.py
```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxdepth = 0
        
        def depth(self, node, now):
            nonlocal maxdepth
            if not node:
                return maxdepth
            
            maxdepth = max(now, maxdepth)
            depth(self, node.left, now+1)
            depth(self, node.right, now+1)
            
            return maxdepth
        
        return depth(self, root, 1)
```

## P Pow(x, n).py
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def tailrec(self, x, n):
            def helper(self, base, x, n):
                # base case
                if n == 0:
                    return 1.0
                if n == 1:
                    return base * x

                # recurrence relation
                if n < 0:
                    return helper(self, base, 1/x, abs(n))
                if n % 2 == 0:
                    return helper(self, base, x**2, n//2)
                else:
                    return helper(self, base*x, x**2, n//2)
            return helper(self, 1, x, n)
        
        return tailrec(self, x, n)
```
[Reference](https://leetcode.com/problems/powx-n/editorial/)
