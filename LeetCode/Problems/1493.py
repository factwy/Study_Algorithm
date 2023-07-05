# Daily challenge in 2023.07.05
# 1493. Longest Subarray of 1's After Deleting One Element
# Difficulty : Medium
# Algorithm : Prefix sum
# Runtime : 378 ms (65.61%), Memory : 20.4 MB (11.96%)
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        if 0 not in nums:
            return n - 1

        prefix = [0] * (n+1)
        for i in range(1, n+1):
            if nums[i-1]:
                prefix[i] = prefix[i-1] + nums[i-1]

        arr = [prefix[n]]
        for i in range(n-1, 0, -1):
            if prefix[i]:
                if prefix[i] < arr[-1]:
                    continue
            arr.append(prefix[i])

        max_len = 0

        len_arr = len(arr)
        for i in range(len_arr):
            if i < len_arr - 2:
                max_len = max(max_len, arr[i] + arr[i+2])
            else:
                max_len = max(max_len, arr[i])

        return max_len
