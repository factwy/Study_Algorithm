# NeetCode - Arrays & Hashing
# 347. Top K Frequent Elements
# Difficulty : Medium
# Algorithm : hash table
# Time complexity : O(N), Space Complexity : O(N)
# Runtime : 121 ms (42.60%), Memory : 21.1 MB (58.58%)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = defaultdict(int)
        for num in nums:
            hash_table[num] += 1

        rank = list(hash_table.items())
        rank.sort(key = lambda x : x[1], reverse = True)

        answer = rank[:k]
        for i in range(len(answer)):
            answer[i] = answer[i][0]

        return answer
