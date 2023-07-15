# NeetCode - Two Pointers
# 11. Container With Most Water
# Difficulty : Medium
# Algorithm : Two Pointers, Sliding Window
# Time complexity : O(N), Space complexity : O(1)
# Runtime : 737 ms (48.31%), Memory : 29.17 MB (88.79%)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0

        start, end = 0, len(height)-1
        while start < end:
            res = max(res, min(height[start], height[end]) * (end - start))

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return res
