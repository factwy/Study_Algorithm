# NeetCode - Tree
# 98. Validate Binary Search Tree
# Difficulty : Medium
# Algorithm : Binary Search Tree
# Time complexity : O(N), Space complexity : O(N)
# Runtime : 50 ms (58.92%), Memory : 19.33 MB (14.08%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Inorder Traversal
        last_val = - float("inf")

        def bst(node):
            nonlocal last_val
            if not node:
                return True

            if not bst(node.left):      # left
                return False

            if last_val >= node.val:    # root
                return False
            last_val = node.val

            if not bst(node.right):     # right
                return False

            return True

        return bst(root)
