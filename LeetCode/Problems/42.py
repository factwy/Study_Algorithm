# NeetCode - Two Pointers
# 42. Trapping Rain Water
# Difficulty : Hard
# Algorithm : Two Pointers, Sliding Window
# Time complexity : O(N), Space complexity : O(1)
# Runtime : 136 ms (60.82%), Memory : 18.16 MB (93.64%)]

class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        start, end = 0, len(height)-1
        max_left, max_right = height[start], height[end]

        while start < end:
            if height[start] < height[end]:
                start += 1
                max_left = max(max_left, height[start])
                res += (max_left - height[start])
            else:
                end -= 1
                max_right = max(max_right, height[end])
                res += (max_right - height[end])

        return res

# reference "sreevardhan____" - Dynamic Programming
# reference "NeetCode " - Two Pointers
