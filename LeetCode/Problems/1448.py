# NeetCode - Tree
# 1448. Count Good Nodes in Binary Tree
# Difficulty : Medium
# Algorithm : Tree, BFS
# Time complexity : O(N), Space complexity : O(N)
# Runtime : 190 ms (69.51%), Memory : 35.05 MB (66.45%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0

        queue = deque()
        queue.append((root, root.val))
        while queue:
            node, max_val = queue.popleft()
            if not node:
                continue

            if node.val >= max_val:
                res += 1
                max_val = node.val

            queue.append((node.left, max_val))
            queue.append((node.right, max_val))

        return res
