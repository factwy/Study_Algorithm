# NeetCode - Stack
# 20. Valid Parentheses
# Difficulty : Easy
# Algorithm : Stack
# Time complexity : O(N), Space Complexity : O(N)
# Runtime : 47 ms (61.86%), Memory : 16.4 MB (14.13%)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_bracket = set(["(", "[", "{"])

        for char in s:
            if char in open_bracket:
                stack.append(char)
            else:
                if not stack:
                    return False
                    
                bracket = stack.pop()
                if 1 <= ord(char) - ord(bracket) <= 2:
                    continue
                return False

        if stack:
            return False
        return True
