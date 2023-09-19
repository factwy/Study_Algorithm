"""
648. Replace Words
Medium
Runtime : 142 ms (62.45%), Memory : 37.80 mb (37.96%)
"""

class TrieNode:
    def __init__(self):
        self.dict = {}
        self.isend = False

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Make TrieNode using dictionary
        head = TrieNode()

        for word in dictionary:
            cur = head
            for c in word:
                if c not in cur.dict.keys():
                    cur.dict[c] = TrieNode()
                cur = cur.dict[c]
            cur.isend = True

        # Replace sentence using TrieNode
        sentence = sentence.split(" ")
        for i in range(len(sentence)):
            cur = head
            num = 0
            for c in sentence[i]:
                if c in cur.dict.keys():
                    cur = cur.dict[c]
                    num += 1
                    if cur.isend:
                        sentence[i] = sentence[i][:num]
                        break
                else:
                    break

        res = " ".join(sentence)
        return res
