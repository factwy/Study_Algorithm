# NeetCode - Sliding Window
# 76. Minimum Window Substring
# Difficulty : Hard
# Algorithm : Sliding Window
# Time complexity : O(N), Space complexity : O(1)
# Runtime : 398 ms (18.68%), Memory : 17.24 MB (25.63%)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # need - Time complexity : O(T), Space complexity : O(1)
        need = {}
        for char in t:
            need[char] = 1 + need.get(char, 0)

        # have - Time complexity : O(S), Space complexity : O(1)
        have = {}
        start = 0
        res = [inf, None, None] # pair : size, start, end
        for i in range(len(s)):
            if s[i] in need.keys():
                have[s[i]] = 1 + have.get(s[i], 0)

            have_num, need_num = have.get(s[start], 0), need.get(s[start], 0)
            while start < i and (s[start] not in need.keys() or have_num > need_num):
                if s[start] in need.keys():
                    have[s[start]] -= 1
                start += 1
                have_num, need_num = have.get(s[start], 0), need.get(s[start], 0)

            ishavebiggerneed = True
            for key in need.keys():
                if have.get(key, 0) < need[key]:
                    ishavebiggerneed = False
                    break

            if ishavebiggerneed:
                if i-start+1 < res[0]:
                    res = [i-start+1, start, i+1]

        if res[2]:
            return s[res[1]:res[2]]
        else:
            return ""
# need to use less time
