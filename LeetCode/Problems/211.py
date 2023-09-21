"""
NeetCode - Trie
211. Design Add and Search Words Data Structure
Difficulty : Medium
Algorithm : Trie
Runtime : 2376 ms (35.85%), Memory : 80.26 MB (67.42%)
"""

class TrieNode:
    def __init__(self):
        self.dict = {}  # char : TrieNode
        self.isend = False

class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.head
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
                
                if c not in cur.dict.keys():
                    return False
                cur = cur.dict[c]
            return cur.isend
        return dfs(0, self.head)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
