# Daily challenge in 2023.07.03
# 859. Buddy Strings
# Difficulty : Easy
# Algorithm : String
# Runtime : 60 ms (12.25%), Memory : 16.5 MB (66.33%)
# Time complexity : O(N), Space complexity : O(1)
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        need_swap_cnt = 0
        need_swap = []
        repetition = [0] * 26

        for i in range(len(s)):
            if s[i] == goal[i]:
                repetition[ord(s[i]) - 97] += 1
            else:
                need_swap_cnt += 1
                need_swap.append([s[i], goal[i]])

        if need_swap_cnt == 2:
            if need_swap[0][1] == need_swap[1][0] and need_swap[1][1] == need_swap[0][0]:
                return True
        if need_swap_cnt == 0:
            if max(repetition) >= 2:
                return True
        return False
