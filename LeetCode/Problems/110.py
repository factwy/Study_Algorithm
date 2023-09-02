# NeetCode - Trees
# 110. Balanced Binary Tree
# Difficulty : Easy
# Algorithm : Tree
# Time complexity : O(N), Space complexity : O(N)
# Runtime : 50 ms (85.18%), Memory : 21.09 MB (74.65%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        
        def check(node):
            nonlocal res
            if not node:
                return 0

            left = check(node.left) + 1
            right = check(node.right) + 1

            if abs(left - right) > 1:
                res = False

            return max(left, right)

        check(root)
        return res
