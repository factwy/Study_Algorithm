"""
NeetCode - Heap / Priority Queue
973. K Closet Points to Origin
Difficulty : Medium
Algorithm : Heap
Time complexity : O(NlogN), Space complexity : O(N)
Runtime : 724 ms (34.87%), Memory : 22.46 MB (71.17%)
"""

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for xy in points:
            dis = xy[0]**2 + xy[1]**2
            heapq.heappush(heap, (dis, xy))
        
        res = []
        for _ in range(k):
            dis, xy = heapq.heappop(heap)
            res.append(xy)
        return res
