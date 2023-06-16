# Daily chailenge in 2023.06.15 (but solved in 2023.06.16)
# 1161. Maximum Level Sum of a Binary Tree
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        Sum, Sum_len = [0], 1
        def maximum(self, node, index):
            nonlocal Sum_len
            if not node:
                return

            if index >= Sum_len:
                Sum.append(node.val)
                Sum_len += 1
            else:
                Sum[index] += node.val

            maximum(self, node.left, index+1)
            maximum(self, node.right, index+1)

        maximum(self, root, 0)
        
        maxSum, maxLevel = Sum[0], 1
        for index, s in enumerate(Sum[1:]):
            if s > maxSum:
                maxSum, maxLevel = s, index+2

        return maxLevel
