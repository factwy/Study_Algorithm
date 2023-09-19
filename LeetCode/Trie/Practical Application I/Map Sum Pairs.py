"""
677. Map Sum Pairs
Medium
Runtime : 40 ms (64.72%), Memory : 16.28 mb (74.17%)
"""

class DictNode:
    def __init__(self):
        self.dict = {}
        self.val = 0

class MapSum:

    def __init__(self):
        self.dictnode = DictNode()

    def insert(self, key: str, val: int) -> None:
        cur = self.dictnode
        for c in key:
            if c not in cur.dict.keys():
                cur.dict[c] = DictNode()
            cur = cur.dict[c]
        cur.val = val


    def sum(self, prefix: str) -> int:
        res, cur = 0, self.dictnode
        for c in prefix:
            if c in cur.dict.keys():
                cur = cur.dict[c]
            else:
                return 0

        queue = deque()
        queue.append(cur)
        while queue:
            node = queue.popleft()
            res += node.val

            for k in node.dict.keys():
                queue.append(node.dict[k])

        return res


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
