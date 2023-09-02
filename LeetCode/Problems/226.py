# NeetCode - Trees
# 226. Invert Binary Tree
# Difficulty : Easy
# Algorithm : Tree
# Time complexity : O(N), Space complexity : O(N)
# Runtime : 38 ms (75.23%), Memory : 16.30 MB (67.89%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left
        return root
