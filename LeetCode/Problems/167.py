# NeetCode - Two Pointers
# 167. Two Sum II - Input Array Is Sorted
# Difficulty : Medium
# Algorithm : Two Pointers, Sliding Window
# Time complexity : O(N), Space complexity : O(1)
# Runtime : 141 ms (56.67%), Memory : 17.1 MB (99.76%)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers)-1

        while start <= end:
            num = numbers[start] + numbers[end]

            if num > target:
                end -= 1
            elif num == target:
                return [start+1, end+1]
            else:
                start += 1
