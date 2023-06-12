# Stack and DFS

## A Stack and DFS
- Depth-first Search(DFS) can be used to find the path from the root node to the target node

## P Number_of_Islands.py
```python
class Solution:
    def numIslands(self, grid: List[List[str]]):
        n, m = len(grid), len(grid[0])
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
        
        def dfs(x, y):
            nonlocal n, m, grid
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if grid[nx][ny] == "1":
                    grid[nx][ny] = "0"
                    dfs(nx, ny)
                    
        cnt = 0
        for x in range(n):
            for y in range(m):
                if grid[x][y] == "1":
                    dfs(x, y)
                    cnt += 1
                    
        return cnt
```

## P Clone_Graph.py
```python

```

## P Target_Sum.py
```python
# brute-force algorithm : Time Limit Exceeded
```

## P Binary_Tree_Inorder_Traversal.py
- try to use dfs
```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
                
        def dfs(node):
            if node.left and node.right:
                return dfs(node.left) + [node.val] + dfs(node.right)
            elif node.left:
                return dfs(node.left) + [node.val]
            elif node.right:
                return [node.val] + dfs(node.right)
            else:
                return [node.val]
            
        answer = dfs(root)
        return answer
```
