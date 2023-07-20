# NeetCode - Sliding Window
# 239. Sliding Window Maximum
# Difficulty : Hard
# Algorithm : Sliding Window
# Time complexity : O(N), Space complexity : O(N)
# Runtime : 2701 ms (5.03%), Memory : 41.36 MB (5.19%)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []   # pair : -num, index
        res = []

        r = 0
        for r in range(k-1):
            heapq.heappush(heap, (-nums[r], r))

        # Time complexity : O(N), Space complexity : O(N)
        for r in range(k-1, len(nums)):
            l = r - (k-1)
            heapq.heappush(heap, (-nums[r], r))

            num, i = heapq.heappop(heap)
            while True:
                if l <= i <= r:
                    break
                num, i = heapq.heappop(heap)

            res.append(-num)
            heapq.heappush(heap, (num, i))

        return res
# need to use less time
