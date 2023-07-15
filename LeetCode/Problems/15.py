# NeetCode - Two Pointers
# 15. 3Sum
# Difficulty : Medium
# Algorithm : Two Pointers, Sliding Window
# Time complexity : O(N^2), Space complexity : O(N)
# Runtime : 1102 ms (90.39%), Memory : 20.43 MB (69.60%)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        size = len(nums)
        nums.sort()

        for i in range(size):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            start, end = i+1, size-1

            while start < end:
                num = nums[i] + nums[start] + nums[end]

                if num > 0:
                    end -= 1
                elif num == 0:
                    answer.append([nums[i], nums[start], nums[end]])
                    start += 1
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                else:
                    start += 1

        return answer
# conference Neetcode and other codes for better solution
