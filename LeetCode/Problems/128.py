# NeetCode - Arrays & Hashing
# 128. Longest Consecutive Sequence
# Difficulty : Medium
# Algorithm : Hash table
# Time complexity : O(N), Space Complexity : O(N)
# Runtime : 504 ms (52.58%), Memory : 35.7 MB (8.70%)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        hash_table = defaultdict(int)
        for num in nums:
            hash_table[num] = 1

        for i in nums:
            next_index = i+1
            while hash_table[next_index]:
                hash_table[i] += hash_table[next_index]
                hash_table[next_index] = 0
                next_index += 1

        return max(hash_table.values())
