# NeetCode - Arrays & Hashing
# 217. Contains Duplicate
# Difficulty : Easy
# Algorithm : Set
# Runtime : 566 ms (27.22%), Memory : 31 MB (55.55%)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counting = set(nums)
        return len(counting) != len(nums)
