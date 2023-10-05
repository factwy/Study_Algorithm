"""
NeetCode - Intervals
56. Merge Interval
Difficulty : Medium
Algorithm : Array
Time complexity : O(NlogN), Space complexity : O(N)
Runtime : 136 ms (62.33%), Memory : 20.92 MB (91.26%)
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        res = []
        start_end = intervals[0]

        for interval in intervals:
            if start_end[1] >= interval[0]:
                start_end[1] = max(start_end[1], interval[1])
            else:
                res.append(start_end)
                start_end = interval
        res.append(start_end)

        return res
