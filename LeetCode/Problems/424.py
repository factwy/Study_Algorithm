# NeetCode - Sliding Window
# 424. Longest Repeating Character Replacement
# Difficulty : Medium
# Algorithm : Sliding Window
# Time complexity : O(N), Space complexity : O(1)
# Runtime : 146 ms (48.45%), Memory : 16.31 MB (80.40%)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        res = 0
        dic = {}

        for end in range(len(s)):
            dic[s[end]] = 1 + dic.get(s[end], 0)
            
            max_value = max(dic.values())
            while (end-start+1) - max_value > k:
                dic[s[start]] -= 1
                start += 1

            res = max(res, end-start+1)

        return res
