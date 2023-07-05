# NeetCode - Arrays & Hashing
# 1. Two Sum
# Difficulty : Easy
# Algorithm : hash table
# Time complexity : O(N), Space Complexity : O(N)
# Runtime : 85 ms (45.88%), Memory : 17.6 MB (35.37%)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, num in enumerate(nums):
            if (target - num) in hash_table.keys():
                answer = [i, hash_table[target-num]]
                return answer
            hash_table[num] = i
