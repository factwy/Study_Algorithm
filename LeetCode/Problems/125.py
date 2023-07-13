# NeetCode - Two Pointers
# 125. Valid Palindrome
# Difficulty : Easy
# Algorithm : Two Pointers, Sliding Window
# Time complexity : O(N), Space complexity : O(1)
# Runtime : 83 ms (14.62%), Memory : 17.1 MB (66.35%)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1

        def isAlphanumeric(self, char):
            if ord("A") <= ord(char) <= ord("Z"):
                return False
            elif ord("a") <= ord(char) <= ord("z"):
                return False
            elif ord("0") <= ord(char) <= ord("9"):
                return False
            return True

        while start <= end:
            front, back = s[start], s[end]

            while isAlphanumeric(self, front) and start < end:
                start += 1
                front = s[start]
            while isAlphanumeric(self, back) and start < end:
                end -= 1
                back = s[end]

            if front.lower() != back.lower():
                return False
            start, end = start+1, end-1

        return True
