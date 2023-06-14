# Daily challenge in 2023.06.14
# 530. Minimum Absolute Difference in BST
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = []
        def traversal(node):
            nonlocal arr
            if not node:
                return

            arr.append(node.val)
            traversal(node.left)
            traversal(node.right)

        traversal(root)
        arr.sort()

        mad = 10**5
        for i in range(len(arr)-1):
            mad = min(mad, abs(arr[i] - arr[i+1]))
        return mad
