"""
NeetCode - Trie
208. Implement Trie (Prefix Tree)
Difficulty : Medium
Algorithm : Trie
Time complexity : O(N), Space complexity : O(N)
Runtime : 154 ms (61.54%), Memory : 33.83 MB (43.61%)
"""

class TrieNode:
  def __init__(self):
    self.dict = {}  # char : TrieNode
    self.isend = False

class Trie:

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.head
        for c in word:
          if c not in cur.dict.keys():
            cur.dict[c] = TrieNode()
          cur = cur.dict[c]
        cur.isend = True

    def search(self, word: str) -> bool:
        cur = self.head
        for c in word:
          if c not in cur.dict.keys():
            return False
          cur = cur.dict[c]
        return cur.isend

    def startsWith(self, prefix: str) -> bool:
        cur = self.head
        for c in prefix:
          if c not in cur.dict.keys():
            return False
          cur = cur.dict[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
