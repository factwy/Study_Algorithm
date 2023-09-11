# Daily challenge in 2023.09.11
# 1282. Group the People Given the Group Size They Belong To
# Difficulty : Medium
# Algorithm : Hash map
# Time complexity : O(N), Space complexity : O(N)
# Runtime : 73 ms (69.53%), Memory : 16.30 MB (99.33%)

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # hashmap : (key - size, value - person)
        hashmap = defaultdict(list)
        for i, size in enumerate(groupSizes):
            hashmap[size].append(i)

        # make group
        res = []
        for key in hashmap.keys():
            arr = []
            for i in range(len(hashmap[key])):
                if i % key == 0 and arr:
                    res.append(arr)
                    arr = []
                
                arr.append(hashmap[key][i])
            if arr:
                res.append(arr)

        return res
