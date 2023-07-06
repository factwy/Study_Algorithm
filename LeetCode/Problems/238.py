# NeetCode - Arrays & Hashing
# 238. Product of Array Except Self
# Difficulty : Medium
# Algorithm : Array
# Time complexity : O(N), Space Complexity : O(N)
# Runtime : 223 ms (95.72%), Memory : 23.1 MB (99.91%)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:     
        if 0 in nums:
            product = 1
            zero_index = []
            for i in range(len(nums)):
                if nums[i]:
                    product *= nums[i]
                    nums[i] = 0
                else:
                    zero_index.append(i)

            if len(zero_index) > 1:
                product = 0

            for index in zero_index:
                nums[index] = product

        else:
            product = 1
            for num in nums:
                product *= num
            for i in range(len(nums)):
                nums[i] = product // nums[i]

        return nums
