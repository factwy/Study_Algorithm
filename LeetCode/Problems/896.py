"""
Daily challenge in 2023.09.29
896. Monotonic Array
Difficulty : Easy
Algorithm : Array
Time complexity : O(N), Space complexity : O(1)
Runtime : 803 ms (87.50%), Memory : 30.37 MB (95.58%)
"""

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isinc, isdec = False, False
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                isdec = True
            elif nums[i] > nums[i-1]:
                isinc = True

            if isdec and isinc:
                return False
        return True
