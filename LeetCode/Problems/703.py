"""
NeetCode - Heap / Priority Queue
703. Kth Largest Element in a Stream
Difficulty : Easy
Algorithm : Heap
Time complexity : O(NlogN + MlogK), Space complexity : O(N)
Runtime : 98 ms (23.95%), Memory : 20.31 MB (55.37%)
"""

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Time complexity : O(NlogN)
        first_heap = []
        for num in nums:
            heapq.heappush(first_heap, -num)

        self.heap = []
        self.k = k
        for _ in range(k):
            if not first_heap:
                break
            heapq.heappush(self.heap, -heapq.heappop(first_heap))

    def add(self, val: int) -> int:
        # Time complexity : O(logK) -> repeat M
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            return self.heap[0]
        num = heapq.heappop(self.heap)

        if val < num:
            heapq.heappush(self.heap, num)
        else:
            heapq.heappush(self.heap, val)
        
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
