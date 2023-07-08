# Daily challenge
# 137. Single Number II
# Difficulty : Medium
# Algorithm : Set
# Time complexity : O(N), Space complexity : O(N)
# Runtime : 69 ms (82.97%), Memory : 19.1 MB (6.38%)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        set_element = set([])
        three_times_element = set([])

        for num in nums:
            if num in three_times_element:
                continue

            if num in set_element:
                three_times_element.add(num)
            else:
                set_element.add(num)

        element = set_element - three_times_element
        answer = list(element)[0]

        return answer
# need different solution with Bit manipluation
