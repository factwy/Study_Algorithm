# Solve Problems Recursively

### A Solve Problems Recursively
a tree can be defined recursively as a node that includes a value and a list of references to children nodes

#### "Top-down" Solution
top-down solution can be considered as a kind of pre-order traversal

```
# top_down(root, params)
1. return sepcific value for null node
2. update the answer if needed
3. left_ans = top_down(root.left, left_params)
4. right_ans = top_down(root.right, right_params)
5. return the answer if needed
```

```python
def maximum_depth(root, depth):
    if root == null:
        return
    if root.left == null and root.right == null:
        answer = max(answer, depth 
    maximum_depth(root.left, depth+1)
    maximum_depth(root.right, depth+1)
```

#### "Bottom-up" Solution
bottom-up solution can be regarded as a kind of post-order traversal

```
# bottom_up(root)
1. return sepcific value for null node
2. left_ans = bottom_up(root.left)
3. right_ans = bottom_up(root.right)
4. return answer
```

```python
def maximum_depth(root):
    if root == null:
        return 0
    left_depth = maximum_depth(root.left)
    right_depth = maximum_depth(root.right)
    return max(left_depth, right_depth) + 1
```

#### Conclusion

1. when we recommended to use "top-down"
>  - can determine some parameters to help the node know its answer
>  - can use these parameters and the value of the node itself to determine what should be the parameters passed to its children

2. when we recommended to use "bottom-up"
>  - can calculate the answer of that node when we know the answer of its children

### A Implemention Maximum Depth of Binary Tree

```python
# top-down solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]):
        answer = 0
        
        def top_down(node, depth):
            nonlocal answer
            if node:
                top_down(node.left, depth+1)
                top_down(node.right, depth+1)
                answer = max(answer, depth)
        
        top_down(root, 1)
        return answer
```

```python
# bottom-up solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]):
        def bottom_up(node):
            if node:
                left_depth = bottom_up(node.left)
                right_depth = bottom_up(node.right)
                return max(left_depth, right_depth) + 1
            else:
                return 0
            
        return bottom_up(root)
```

### A Implemention Symmetric Tree

```python
# top-down solution
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]):
        answer = True
        
        def top_down(left_node, right_node):
            nonlocal answer
            
            if left_node and right_node:
                if left_node.val != right_node.val:
                    answer = False
                    
                outside_left = left_node.left
                outside_right = right_node.right

                inside_right = right_node.left
                inside_left = left_node.right

                top_down(outside_left, outside_right)
                top_down(inside_left, inside_right)
            elif left_node:
                answer = False
            elif right_node:
                answer = False
            
        top_down(root.left, root.right)
        return answer
```

```python
# bottom-up solution
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]):
        
        def bottom_up(left_node, right_node):
            if left_node and right_node:
                if left_node.left == left_node.right == right_node.left == right_node.right == None:
                    if left_node.val == right_node.val:
                        return True
                    else:
                        return False
            elif left_node == None and right_node == None:
                return True
            else:
                return False
                
            check1 = bottom_up(left_node.left, right_node.right)
            check2 = bottom_up(left_node.right, right_node.left)
            
            if check1 & check2 & (left_node.val == right_node.val):
                return True
            else:
                return False
            
        return bottom_up(root.left, root.right)
```

### A Implemention Path Sum

```python
# top-down solution
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int):
        answer = False
        
        def top_down(node, pathsum):
            nonlocal answer 
            
            if node and node.left == None and node.right == None:
                if pathsum + node.val == targetSum:
                    answer = True
            
            if node:
                top_down(node.left, pathsum + node.val)
                top_down(node.right, pathsum + node.val)
            
        top_down(root, 0)
        return answer
```
