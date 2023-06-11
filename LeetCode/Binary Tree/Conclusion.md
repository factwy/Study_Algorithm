# Conclusion

## P Construct Binary Tree from Inorder and Postorder Traversal
```python
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]):
        if not inorder:
            return None
        
        root = postorder.pop()
        tree = TreeNode(root)
        
        root_index = inorder.index(root)

        tree.right = Solution.buildTree(self, inorder[(root_index+1):], postorder)
        tree.left = Solution.buildTree(self, inorder[:root_index], postorder)
        
        return tree
```
[**helped solution**](https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/942/discuss/3302159/Easy-Solutions-in-Java-Python-and-C++-Look-at-once)

## P Construct Binary Tree from Preorder and Inorder Traversal
```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]):
        if not inorder:
            return None
        
        root = preorder[0]
        preorder.remove(root)
        tree = TreeNode(root)
        
        inorder_index = inorder.index(root)
        
        tree.left = Solution.buildTree(self, preorder, inorder[:inorder_index])
        tree.right = Solution.buildTree(self, preorder, inorder[(inorder_index+1):])
        
        return tree
```
