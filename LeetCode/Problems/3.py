# NeetCode - Sliding Window
# 3. Longest Substring Without Repeating Characters
# Difficulty : Medium
# Algorithm : Sliding Window
# Time complexity : O(N), Space complexity : O(N)
# Runtime : 91 ms (31.52%), Memory : 16.52 MB (13.07%)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l, r = 0, 0
        substring = set([])
        while r < len(s):
            if s[r] in substring:
                substring.remove(s[l])
                l += 1
            else:
                substring.add(s[r])
                r += 1
            res = max(res, len(substring))

        return res
