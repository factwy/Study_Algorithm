# Daily challenge in 2023.08.10
# 81. Search in Rotated Sorted Array II
# Difficulty : Medium
# Algorithm : Binary Search
# Time complexity : O(logN), Space complexity : O(logN)
# Runtime : 55 ms (93.46%), Memory : 17.4 MB (11.93%)

class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        def binary_search(self, l, r):
            nonlocal target
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return True

                if nums[l] == nums[mid] == nums[r]:
                    # duplicate
                    return (binary_search(self, l, mid-1) | binary_search(self, mid+1, r))

                if nums[l] > nums[mid]:
                    # left ~ mid : rotated sorted array
                    # mid ~ right : sorted array
                    if target > nums[mid]:
                        if target <= nums[r]:
                            l = mid + 1
                        else:
                            r = mid - 1
                    else:
                        r = mid - 1
                else:
                    # left ~ mid : sorted array
                    # mid ~ right : rotated sorted array
                    if target > nums[mid]:
                        l = mid + 1
                    else:
                        if nums[l] <= target:
                            r = mid - 1
                        else:
                            l = mid + 1
            
            return False

        return binary_search(self, 0, len(nums)-1)
