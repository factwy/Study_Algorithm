# Daily challenge in 2023.07.10
# 111. Minimum Depth of Binary Tree
# Difficulty : Easy
# Algorithm : Depth-first Search, Tree
# Time complexity : O(N), Space complexity : O(N)
# Runtime : 516 ms (80.99%), Memory : 52.3 MB (72.26%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def traversal(self, node = root, depth = 1):
            nonlocal min_depth
            if node.left == node.right == None:
                min_depth = min(depth, min_depth)
                
            if node.left and depth < min_depth:
                traversal(self, node.left, depth+1)
            if node.right and depth < min_depth:
                traversal(self, node.right, depth+1)

        if not root:
            return 0

        min_depth = 10**5
        traversal(self)

        return min_depth
