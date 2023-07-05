# NeetCode - Arrays & Hashing
# 49. Group Anagrams
# Difficulty : Medium
# Algorithm : array
# Time complexity : O(N^2), Space Complexity : O(N)
# Runtime : 1618 ms (5.2%), Memory : 21.4 MB (34.69%)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counting_group = []
        anagram_group = []

        for string in strs:
            counting = [0] * 26
            for s in string:
                counting[ord(s) - ord('a')] += 1

            if not counting_group:
                counting_group.append(counting)
                anagram_group.append([string])
            else:
                isanagramgroup = True
                if counting in counting_group:
                    anagram_group[counting_group.index(counting)].append(string)
                else:
                    counting_group.append(counting)
                    anagram_group.append([string])

        return anagram_group
