# NeetCode - Trees
# 543. Diameter of Binary Tree
# Difficulty : Easy
# Algorithm : Tree
# Time complexity : O(N), Space complexity : O(N)
# Runtime : 57 ms (39.65%), Memory : 18.66 MB (69.03%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dia = 0
        def diameter(node):
            nonlocal max_dia
            if not node:
                return 0

            max_left_depth = diameter(node.left)
            max_right_depth = diameter(node.right)

            max_dia = max(max_dia, max_left_depth + max_right_depth)

            return max(max_left_depth, max_right_depth) + 1

        diameter(root)
        return max_dia
