# NeetCode - Binary Search
# 704. Binary Search
# Difficulty : Easy
# Algorithm : Binary search
# Time complexity : O(logN), Space complexity : O(1)
# Runtime : 256 ms (19.41%), Memory : 17.57 MB (99.92%)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1
