"""
208. Implement Trie (Prefix Tree)
Medium
Runtime : 154 ms (64.64%), Memory : 33.6 mb (74.18%)
"""

class TreeNode:
    def __init__(self):
        self.children = {}  # character : corresponding children node (char : TreeNode)
        self.isEnd = False

class Trie:

    def __init__(self):
        self.head = TreeNode()

    def insert(self, word: str) -> None:
        cur = self.head
        for c in word:
            if c not in cur.children.keys():
                cur.children[c] = TreeNode()
            cur = cur.children[c]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.head
        for c in word:
            if c not in cur.children.keys():
                return False
            cur = cur.children[c]
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.head
        for c in prefix:
            if c not in cur.children.keys():
                return False
            cur = cur.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
