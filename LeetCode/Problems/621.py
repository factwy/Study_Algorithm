"""
NeetCode - Heap / Priority Queue
621. Task Scheduler
Difficulty : Medium
Algorithm : Heap
Time complexity : O(NlogN), Space complexity : O(N)
Runtime : 529 ms (55.89%), Memory : 16.9 MB (69.19%)
"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = {}
        for task in tasks:
            if task in dic.keys():
                dic[task] += 1
            else:
                dic[task] = 1

        heap = []
        for val in dic.values():
            heapq.heappush(heap, -val)

        cnt = 0
        while heap:
            arr = [heapq.heappop(heap)]
            for _ in range(n):
                if heap:
                    arr.append(heapq.heappop(heap))
            
            cnt += (n+1)
            for num in arr:
                if num == -1:
                    continue
                heapq.heappush(heap, num+1)

            if not heap:
                cnt -= (n+1 - len(arr))
        return cnt
