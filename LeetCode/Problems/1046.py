"""
NeetCode - Heap / Priority Queue
1046. Last Stone Weight
Difficulty : Easy
Algorithm : Heap
Time complexity : O(NlogN), Space complexity : O(N)
Runtime : 38 ms (67.95%), Memory : 16.21 MB (58.18%)
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            st1 = heapq.heappop(heap)
            st2 = heapq.heappop(heap)

            if st1 != st2:
                heapq.heappush(heap, -abs(st1 - st2))

        return -heap[0] if heap else 0
