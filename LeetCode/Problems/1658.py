"""
Daily challenge in 2023.09.20
1658. Minimum Operations to Reduce X to Zero
Difficulty : Medium
Algorithm : Sliding Window
Time complexity : O(N), Space complexity : O(N)
Runtime : 1181 ms (14.79%), Memory : 30.23 MB (83.06%)
"""

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        find_num = sum(nums) - x
        start, end = 0, 1
        prefix = [0] * (len(nums)+1)
        for i in range(1, len(nums)+1):
            prefix[i] = prefix[i-1] + nums[i-1]

        cnt = -1
        while start <= end and start <= len(nums):
            res = prefix[end] - prefix[start]
            if res == find_num:
                cnt = min(cnt, len(nums) - (end-start)) if cnt != -1 else len(nums) - (end-start)

            if res > find_num:
                start += 1
            else:
                if end < len(nums):
                    end += 1
                else:
                    break
                
        return cnt
