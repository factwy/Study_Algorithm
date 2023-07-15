# Daily challenge
# 1218. Longest Arithmetic Subsequence of Given Difference
# Difficulty : Medium
# Algorithm : Hash Table
# Time complexity : O(N), Space complexity : O(N)
# Runtime : 599 ms (25.68%), Memory : 30.29 MB (9.11%)
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        table = defaultdict(int)

        for num in arr[::-1]:
            table[num] = max(table[num], table[num+difference]+1)

        return max(table.values())
