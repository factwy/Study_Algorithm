# NeetCode - Stack
# 739. Daily Temperatures
# Difficulty : Medium
# Algorithm : Stack, Monotonic Stack
# Time complexity : O(N), Space complexity : O(N)
# Runtime : 1342 ms (50.69%), Memory : 31.9 MB (23.92%)
# reference NeetCode
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                answer[stackInd] = (i - stackInd)
            stack.append([t, i])

        return answer
