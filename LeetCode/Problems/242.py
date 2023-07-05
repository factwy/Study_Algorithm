# NeetCode - Arrays & Hashing
# 242. Valid Anagram
# Difficulty : Easy
# Algorithm : array
# Time complexity : O(N), Space Complexity : O(1)
# Runtime : 74 ms (29.81%), Memory : 16.9 MB (63.71%)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s, count_t = [0]*26, [0]*26
        for i in range(len(s)):
            count_s[ord(s[i]) - ord('a')] += 1
            count_t[ord(t[i]) - ord('a')] += 1

        return count_s == count_t
