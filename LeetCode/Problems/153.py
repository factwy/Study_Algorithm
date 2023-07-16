# NeetCode - Binary Search
# 153. Find Minimum in Rotated Sorted Array
# Difficulty : Medium
# Algorithm : Binary search
# Time complexity : O(N), Space complexity : O(1)
# Runtime : 53 ms (77.76%), Memory : 16.72 MB (12.62%)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return min(nums)

        l, r = 0, len(nums)-1
        edge = max(nums[l], nums[r])
        
        while l <= r:
            mid = (l + r) // 2

            num = nums[mid]

            if num < nums[mid-1] and num < nums[(mid % (len(nums)-1))+1]:
                return num
            else:
                if num >= edge:
                    l = mid + 1
                else:
                    r = mid - 1
