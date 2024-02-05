"""
Daily challenge in 2024.02.05
387. First Unique character in a String
Difficulty : Easy
Algorithm : Hasp Table
Time complexity : O(N), Space complexity : O(N)
Runtime : 94 ms (61.17%), Memory : 17.07 MB (55.07%)
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        table = {}

        for i, a in enumerate(s):
            if a in table.keys():
                table[a] = 10**5
            else:
                table[a] = i

        res = min(table.values())
        return res if res != 10**5 else -1
