# NeetCode - Sliding Window
# 76. Minimum Window Substring
# Difficulty : Hard
# Algorithm : Sliding Window
# Time complexity : O(N), Space complexity : O(1)
# Runtime : 137 ms (74.17%), Memory : 17.16 MB (65.01%)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # need - Time complexity : O(T), Space complexity : O(1)
        # have - Time complexity : O(S), Space complexity : O(1)
        need, have = {}, {}
        for char in t:
            need[char] = 1 + need.get(char, 0)

        need_num, have_num = len(need), 0
        start = 0
        res = [inf, None, None] # pair : size, start, end
        for i in range(len(s)):
            have[s[i]] = 1 + have.get(s[i], 0)

            if s[i] in need and have[s[i]] == need[s[i]]:
                have_num += 1

            # Once all the characters are covered, move the left pointer
            if have_num == need_num:
                while start < i:
                    have[s[start]] -= 1

                    if s[start] in need and have[s[start]] < need[s[start]]:
                        have_num -= 1
                        break

                    start += 1

                if i-start+1 < res[0]:
                    res = [i-start+1, start, i+1]
                start += 1

        if res[2]:
            return s[res[1]:res[2]]
        else:
            return ""
