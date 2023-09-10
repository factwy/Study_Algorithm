# NeetCode - Tree
# 230. Kth Smallest Element in a BST
# Difficulty : Medium
# Algorithm : Binary Search Tree
# Time complexity : O(N), Space complexity : O(N)
# Runtime : 60 ms (37.23%), Memory : 20.38 MB (87.34%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i, res = 0, 0

        def bst(node):          # Inorder Traversal
            nonlocal i, res
            if not node:
                return

            bst(node.left)      # left
            
            i += 1              # root
            if i == k:
                res = node.val
                return

            bst(node.right)     # right

        bst(root)
        return res
