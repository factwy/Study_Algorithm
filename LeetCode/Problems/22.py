# NeetCode - Stack
# 22. Generate Parentheses
# Difficulty : Medium
# Algorithm : Stack
# Runtime : 43 ms (91.76%), Memory : 16.7 MB (26.49%)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def rec(self, arr = "(", left = 1, right = 0):
            nonlocal n, answer

            if left == right == n:
                answer.append(arr)
                return

            if left < n:
                rec(self, arr+"(", left+1, right)
            if right < left:
                rec(self, arr+")", left, right+1)

        answer = []
        rec(self)

        return answer

# reference solution [IdealYuvi]
