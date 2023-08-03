# Daily challenge in 2023.08.03
# 17. Letter Combinations of a Phone Number
# Difficulty : Medium
# Algorithm : Backtracking
# Time complexity : O(4^N), Space complexity : O(N)
# Runtime : 41 ms (81.43%), Memory : 16.25 MB (86.05%)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
        res = []
        
        def digit_to_letter(self, digit, string = ""):
            nonlocal res

            if not digit:
                if string:
                    res.append(string)
                return

            for letter in letters[digit[0]]:
                digit_to_letter(self, digit[1:], string+letter)

        digit_to_letter(self, digits)
        return res
