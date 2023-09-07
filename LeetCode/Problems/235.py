# NeetCode - Linked List
# 235. Lowest Common Ancestor of a Binary Search Tree
# Difficulty : Medium
# Algorithm : Linked List
# Time complexity : O(logN), Space complexity : O(1)
# Runtime : 79 ms (47.21%), Memory : 20.87 MB (57.20%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        res = root
        while root:
            if p.val <= root.val <= q.val:
                return root

            if p.val > root.val:
                root = root.right
            elif q.val < root.val:
                root = root.left

        return res
