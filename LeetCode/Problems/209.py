# Daily challenge in 2023.07.06
# 209. Minimum Size Subarray Sum
# Difficulty : Medium
# Algorithm : Sliding Window
# Time complexity : O(N), Space complexity : O(N)
# Runtime : 286 ms (17.24%), Memory : 29.4 MB (9.10%)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = 10**9

        subarray = deque()
        subarray_sum = 0

        for num in nums:
            subarray_sum += num
            subarray.append(num)

            while subarray:
                if subarray_sum - subarray[0] >= target:
                    subarray_sum -= subarray.popleft()
                else:
                    break

            if subarray_sum >= target:
                min_len = min(min_len, len(subarray))

        if min_len == 10**9:
            min_len = 0
            
        return min_len
