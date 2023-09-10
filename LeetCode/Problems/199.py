# NeetCode - Tree
# 199. Binary Tree Right Side View
# Difficulty : Medium
# Algorithm : Tree, BFS
# Time complexity : O(N), Space complexity : O(N)
# Runtime : 35 ms (90.01%), Memory : 16.32 MB (39.59%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        queue = deque()
        queue.append((root, 0))
        while queue:
            node, f = queue.popleft()
            if not node:
                continue

            if len(res) == f:
                res.append(node.val)
            else:
                res[f] = node.val

            queue.append((node.left, f+1))
            queue.append((node.right, f+1))

        return res
