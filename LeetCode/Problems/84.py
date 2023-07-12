# NeetCode - Stack
# 84. Largest Rectangle in Histogram
# Difficulty : Hard
# Algorithm : Stack
# Time complexity : O(N), Space complexity : O(N)
# Runtime : 948 ms (54.41%), Memory : 36.5 MB (5.21%)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # pair : index, height
        max_val = 0

        for index, height in enumerate(heights):
            if not stack:
                stack.append([index, height])
                continue

            i = index
            while stack and height < stack[-1][1]:
                pre_val = stack.pop()
                max_val = max(max_val, pre_val[1] * (index - pre_val[0]))
                i = pre_val[0]

            stack.append([i, height])

        size = len(heights)
        while stack:
            index, height = stack.pop()
            max_val = max(max_val, height * (size - index))

        return max_val
# reference NeetCode
