# Daily challenge in 2023.08.14
# 215. Kth Largest Element in an Array
# Difficulty : Medium
# Algorithm : Heap
# Time complexity : O(NlogN), Space complexity : O(N)
# Runtime : 467 ms (81.84%), Memory : 29.90 MB (37.07%)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)

        for _ in range(k-1):
            heapq.heappop(heap)

        return -heapq.heappop(heap)
