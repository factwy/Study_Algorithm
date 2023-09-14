# Insertion in Trie

```python
cur = root
for c in S:
  if c not in cur.children.keys():
    cur.children[c] = TrieNode()
  cur = cur.children[c]
```

- Remember to initialize a root node before you insert the strings

# Search in Trie

```python
cur = root
for c in S:
  if c not in cur.children.keys():
    return False
  c = c.children[c]
return True
```

- If search is False, the target word is definitely not in the Trie
- If search is True, we need to check if the target word is only a prefix of words in Trie or it is exactly a word
