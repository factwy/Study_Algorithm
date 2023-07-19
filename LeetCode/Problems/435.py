# Daily challenge in 2023.07.19
# 435. Non-overlapping Intervals
# Difficulty : Medium
# Algorithm : Greedy
# Time complexity : O(NlogN), Space complexity : O(N)
# Runtime : 1337 ms (74.07%), Memory : 55.37 MB (48.43%)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0

        # Time complexity : O(NlogN), Spacec complexity : O(N)
        intervals.sort(key = lambda x: x[1])
        res = 0

        # Time complexity : O(N), Space complexity : O(1)
        num = intervals[0][1]
        for start, end in intervals[1:]:
            if start < num:
                res += 1
            else:
                num = end

        return res
        
# reference Editorial
# my wrong code : intervals.sort() -> intervals.sort(key = lambda x: x[1])
# For start and num determine res, it need condition which is always end greater than or equal to num
