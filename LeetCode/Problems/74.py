# NeetCode - Binary Search
# 74. Search a 2D Matrix
# Difficulty : Medium
# Algorithm : Binary search
# Time complexity : O(log M*N), Space complexity : O(1)
# Runtime : 53 ms (89.48%), Memory : 16.92 MB (27.92%)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_l, row_r = 0, len(matrix)-1
        l, r = 0, len(matrix[0])-1

        row = 0
        while row_l <= row_r:
            row = (row_l + row_r) // 2
            if matrix[row][l] <= target <= matrix[row][r]:
                break
            elif matrix[row][r] < target:
                row_l = row + 1
            else:
                row_r = row - 1

        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False
