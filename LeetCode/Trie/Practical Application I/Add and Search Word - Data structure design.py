"""
211. Design Add and Search Words Data structure
Medium
Runtime : 3350 ms (12.39%), Memory : 80.7 mb (17.37%) -> BFS
Runtime : 2469 ms (30.99%), Memory : 80.34 mb (52.80%) -> DFS (reference sample submission)
"""

# Solution - BFS
class TrieNode:
    def __init__(self):
        self.dict = {}  # char : TrieNode
        self.isend = False

class WordDictionary:

    def __init__(self):
        self.wd = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.wd
        for c in word:
            if c not in cur.dict.keys():
                cur.dict[c] = TrieNode()
            cur = cur.dict[c]
        cur.isend = True

    def search(self, word: str) -> bool:
        queue = deque()
        queue.append((0, self.wd))  # index, TrieNode

        while queue:
            index, cur = queue.popleft()
            if index == len(word):
                if cur.isend:
                    return True
                else:
                    continue

            if word[index] == ".":
                for key in cur.dict.keys():
                    queue.append((index+1, cur.dict[key]))
            else:
                if word[index] not in cur.dict.keys():
                    continue
                queue.append((index+1, cur.dict[word[index]]))
        
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

"""
# Solution - DFS (Reference sample submission)

class TrieNode:
    def __init__(self):
        self.dict = {}  # char : TrieNode
        self.isend = False

class WordDictionary:

    def __init__(self):
        self.wd = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.wd
        for c in word:
            if c not in cur.dict.keys():
                cur.dict[c] = TrieNode()
            cur = cur.dict[c]
        cur.isend = True

    def search(self, word: str) -> bool:
        def dfs(index, cur):
            for i in range(index, len(word)):
                c = word[i]
                if c == ".":
                    for next in cur.dict.values():
                        if dfs(i+1, next):
                            return True
                    return False
                else:
                    if c not in cur.dict.keys():
                        return False
                    cur = cur.dict[c]
            return cur.isend

        return dfs(0, self.wd)
"""
