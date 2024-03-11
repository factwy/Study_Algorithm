"""
Daily challenge in 2024.03.11
791. Custom Sort String
Difficulty : Medium
Algorithm : Hash Table, Sort
Time complexity : O(NlogN), Space complexity : O(N)
Runtime : 34 ms (68.03%), Memory : 16.54 MB (61.09%)
"""

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        if(len(s) == 1):
            return s

        ordering = {}
        for i, c in enumerate(order):
            ordering[c] = i

        non_order = ""
        res = []
        for c in s:
            if c not in ordering.keys():
                non_order += c
            else:
                res.append(c)

        res.sort(key = lambda x : ordering[x])
        res = "".join(res) + non_order
        
        return res
