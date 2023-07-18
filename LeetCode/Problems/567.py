# NeetCode - Sliding Window
# 567. Permutation in String
# Difficulty : Medium
# Algorithm : Sliding Window
# Time complexity : O(N), Space complexity : O(1)
# Runtime : 67 ms (97.68%), Memory : 16.56 MB (23.52%)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        dict_s1, dict_s2 = {}, {}
        for i in range(len(s1)):
            dict_s1[s1[i]] = 1 + dict_s1.get(s1[i], 0)
            dict_s2[s2[i]] = 1 + dict_s2.get(s2[i], 0)

        if dict_s1 == dict_s2:
            return True

        for i in range(len(s1), len(s2)):
            dict_s2[s2[i]] = 1 + dict_s2.get(s2[i], 0)
            dict_s2[s2[i - len(s1)]] -= 1
            if not dict_s2[s2[i - len(s1)]]:
                dict_s2.pop(s2[i - len(s1)])

            if dict_s1 == dict_s2:
                return True
        return False
