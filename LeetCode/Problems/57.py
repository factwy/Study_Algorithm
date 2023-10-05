"""
NeetCode - Intervals
57. Insert Interval
Difficulty : Medium
Algorithm : Queue
Time complexity : O(N), Space complexity : O(N)
Runtime : 80 ms (72.69%), Memory : 19.90 MB (32.38%)
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        queue = deque()
        for interval in intervals:
            if newInterval and newInterval[0] < interval[0]:
                queue.append(newInterval)
                newInterval = None
            queue.append(interval)
        if newInterval:
            queue.append(newInterval)

        res = []
        start_end = queue.popleft()
        while queue:
            interval = queue.popleft()
            
            if start_end[1] >= interval[0]:
                start_end[1] = max(start_end[1], interval[1])
            else:
                res.append(start_end)
                start_end = interval
        res.append(start_end)

        return res
