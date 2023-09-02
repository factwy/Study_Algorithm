# NeetCode - Trees
# 104. Maximum Depth of Bianrny Tree
# Difficulty : Easy
# Algorithm : Tree
# Time complexity : O(N), Space complexity : O(N)
# Runtime : 49 ms (58.98%), Memory : 18.71 MB (31.50%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode], depth = 0) -> int:
        if not root:
            return depth

        depth = max(self.maxDepth(root.left, depth), self.maxDepth(root.right, depth)) + 1
        return depth
