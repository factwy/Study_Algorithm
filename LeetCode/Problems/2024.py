# Daily challenge in 2023.07.07
# 2024. Maximize the Confusion of an Exam
# Difficulty : Medium
# Algorithm : Sliding Window
# Time complexity : O(N), Space complexity : O(1)
# Runtime : 596 ms (14.32%), Memory : 16.6 MB (99.9%)
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        def counting(self, boolean):
            nonlocal max_confusion, answerKey, k
            start, end = 0, 0
            not_boolean = 0

            while start <= end and end < len(answerKey):
                if answerKey[end] != boolean:
                    not_boolean += 1

                while not_boolean > k and start <= end:
                    if answerKey[start] != boolean:
                        not_boolean -= 1
                    start += 1

                max_confusion = max(max_confusion, end-start+1)

                end += 1


        max_confusion = 0
        counting(self, "T")
        counting(self, "F")

        return max_confusion
