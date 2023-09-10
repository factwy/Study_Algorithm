# NeetCode - Tree
# 102. Binary Tree Level Order Traversal
# Difficulty : Medium
# Algorithm : Linked List
# Time complexity : O(N), Space complexity : O(1)
# Runtime : 44 ms (74.42%), Memory : 16.88 MB (99.05%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque()

        queue.append((root, 0)) # TreeNode, floor
        while queue:
            node, f = queue.popleft()

            if not node:
                continue

            if len(res) == f:
                res.append([])

            res[-1].append(node.val)
            queue.append((node.left, f+1))
            queue.append((node.right, f+1))

        return res
