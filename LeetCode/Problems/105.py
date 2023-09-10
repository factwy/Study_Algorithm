# NeetCode - Tree
# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Difficulty : Medium
# Algorithm : Tree
# Time complexity : O(N), Space complexity : O(N)
# Runtime : 157 ms (63.84%), Memory : 90.8 MB (41.86%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        head = TreeNode(preorder[0])

        i = inorder.index(preorder[0])

        head.left = self.buildTree(preorder[1:(i+1)], inorder[:i])
        head.right = self.buildTree(preorder[(i+1):], inorder[(i+1):])

        return head
