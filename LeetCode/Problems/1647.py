"""
Daily challenge in 2023.09.11
1282. Minimum Deletions to Make Character Frequencies Unique
Difficulty : Medium
Algorithm : Hash map
Time complexity : O(N), Space complexity : O(N)
Runtime : 112 ms (83.78%), Memory : 17.18 MB (62.10%)
"""

class Solution:
    def minDeletions(self, s: str) -> int:
        count = collections.Counter(s)
        
        fre = set([])
        res = 0
        for c in count:
            num = count[c]
            while num and num in fre:
                res += 1
                num -= 1
            fre.add(num)

        return(res)

"""
First Code
Algorithm : Heap
Time complexity : O(NlogN), Space complexity : O(N)
Runtime : 419 ms (5.3%), Memory : 17 MB (99.72%)

class Solution:
    def minDeletions(self, s: str) -> int:
        count = {}
        for c in s:
            count[ord(c)-97] = count[ord(c)-97] - 1 if (ord(c)-97) in count.keys() else -1

        heap = []
        for num in count.values():
            heapq.heappush(heap, num)
        res = 0

        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            while x == y and y < 0:
                res += 1
                heapq.heappush(heap, y+1)
                y = heapq.heappop(heap)
            heapq.heappush(heap, y)

        return res
"""
