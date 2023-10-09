"""
Daily challenge in 2023.10.09
34. Find First and Last Position of Element in Sorted Array
Difficulty : Medium
Algorithm : Binary Search
Time complexity : O(logN), Space complexity : O(1)
Runtime : 77 ms (91.12%), Memory : 17.66 MB (84.76%)
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        # Find target position
        start, end = 0, len(nums)-1
        pos = 0
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                pos = mid
                break
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        if nums[pos] != target:
            return [-1, -1]

        # Find First position
        start, end = 0, pos
        first = 0
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            else:
                if nums[mid] == target:
                    first = mid
                end = mid - 1
        if nums[first] != target:
            return [-1. -1]

        # Find Last position
        start, end = pos, len(nums)-1
        second = 0
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid - 1
            else:
                if nums[mid] == target:
                    second = mid
                start = mid + 1

        if nums[second] != target:
            return [-1, -1]
        return [first, second]
