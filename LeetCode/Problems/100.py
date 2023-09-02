# NeetCode - Trees
# 100. Same Tree
# Difficulty : Easy
# Algorithm : Tree
# Time complexity : O(N), Space complexity : O(N)
# Runtime : 33 ms (92.03%), Memory : 16.26 MB (85.69%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = True

        def check(node1, node2):
            nonlocal res
            if node1 == node2:  # except the moment node1 and node2 are None
                return
            if not node1 or not node2:
                res = False     # if node1 is None or node2 is None -> Not same tree
            elif node1.val != node2.val:
                res = False     # if node1.val is not equal node2.val -> Not same tree

            if not res:
                return
            check(node1.left, node2.left)
            check(node1.right, node2.right)

        check(p, q)
        return res
