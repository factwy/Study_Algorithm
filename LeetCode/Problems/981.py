# NeetCode - Binary Search
# 981. Time Based Key-Value Store
# Difficulty : Medium
# Algorithm : Binary search, Hash table
# Time complexity : O(MlogN), Space complexity : O(MN)
# - M : the number of key, N : the number of call "set"
# Runtime : 855 ms (18.23%), Memory : 74.76 MB (34.13%)
class TimeMap:

    def __init__(self):
        self.hashtable = {}     # hashtable[key] = index
        self.arr = []           # arr[index] = [[key, value] ...]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashtable.keys():
            self.arr[self.hashtable[key]].append([timestamp, value])
        else:
            self.hashtable[key] = len(self.hashtable)
            self.arr.append([[timestamp, value]])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashtable.keys():
            return ""
            
        key_arr = self.arr[self.hashtable[key]]
        l, r = 0, len(key_arr)-1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if key_arr[mid][0] == timestamp:
                return key_arr[mid][1]
            elif key_arr[mid][0] > timestamp:
                r = mid - 1
            else:
                res = key_arr[mid][1]
                l = mid + 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
