# Traverse A Tree

### A Traverse a Tree - Introduction

- Pre-order Traversal : visit the root first. Then traverse the left subtree. Finally, traverse the right subtree
- In-order Traversal : traverse the left subtree first. Then visit the root. Finally, traverse the right subtree
- Post-order Traversal : traverse the left subtree first. Then traverse the right subtree. Fianlly, visit the root

- In-order Traversal is used in binary search tree
- Post-order Traversal is uesd in deletion process or mathematical expressions

### A Implemention Binary Tree preorder Traversal
- Pre-order Traversal : root > left > right
```python
# Recursive solution
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]):
        output = []
        if root != None:
            output += [root.val]
            if root.left != None:
                output += Solution.preorderTraversal(self, root.left)
            if root.right != None:
                output += Solution.preorderTraversal(self, root.right)
        return output
```

```python
# Iterative solution
Optional[TreeNode]):
        output = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                output.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
            
        return output
```

### A Implemention Binary Tree Inorder Traversal
- In-order Traversal : left > root > right
```python
# Recursive solution
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]):
        answer = []
        
        def dfs(node):
            if node:
                if node.left:
                    dfs(node.left)
                answer.append(node.val)
                if node.right:
                    dfs(node.right)
        
        dfs(root)
        return answer
```

```python
# Iterative solution
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]):
        answer = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            if type(node) == int:
                answer.append(node)
            elif node:
                stack.append(node.right)
                stack.append(node.val)
                stack.append(node.left)
            
        return answer
```

### A Implemention Binary Tree Postorder Traversal
- Post-order Traversal : left > right > root

```python
# Recursive solution
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]):
        answer = []
        
        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                answer.append(node.val)
                
        dfs(root)
        return answer
```

```python
# Iterative solution
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]):
        answer = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            if type(node) == int:
                answer.append(node)
            elif node:
                stack.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
                
        return answer
```

### A Level-order Traversal - Introduction
- Level-order Traversal : traverse the tree level by level
- Breadth-First Search starts with a root node and visit the node itself first. Then traverse its neighbors. traverse its second level neighbors, traverse its third level neighbors, so on and so forth
