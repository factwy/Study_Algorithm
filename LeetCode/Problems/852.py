# Daily challenge in 2023.07.25
# 852. Peak Index in a Mountain Array
# Difficulty : Medium
# Algorithm : Binary Search
# Time complexity : O(logN), Space complexity : O(1)
# Runtime : 590 ms (73.38%), Memory : 30.08 MB (63.67%)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # Time complexity : O(logN), Space complexity : O(1)
        l, r = 0, len(arr)-1
        while l <= r:
            mid = (l + r) // 2

            if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] < arr[mid+1]:
                l = mid + 1
            else:
                r = mid - 1
