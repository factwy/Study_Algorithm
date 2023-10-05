"""
Daily challenge in 2023.10.05
229. Majority Element II
Difficulty : Medium
Algorithm : Hash Table
Time complexity : O(1), Space complexity : O(N)
Runtime : 108 ms (72.53%), Memory : 17.57 MB (97.53%)
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        element = defaultdict(int)
        res = set([])

        for num in nums:
            element[num] += 1

            if num not in res and element[num] > (len(nums) / 3):
                res.add(num)

        return list(res)
