# NeetCode - Two Pointers
# 42. Trapping Rain Water
# Difficulty : Hard
# Algorithm : Dynamic Programming
# Time complexity : O(N), Space complexity : O(N)
# Runtime : 162 ms (16.47%), Memory : 18.64 MB (37.38%)
class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        left, right = [0] * size, [0] * size
        left[0], right[size-1] = height[0], height[size-1]

        for i in range(1, size):
            left[i] = max(left[i-1], height[i])
            right[size-1-i] = max(right[size-i], height[size-1-i])

        res = 0
        for i, h in enumerate(height):
            res += min(left[i], right[i]) - h
        
        return res
# reference solution by "sreevardhan____"
