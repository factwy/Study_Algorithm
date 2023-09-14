# Introduction to Trie

## Trie is
- a special form of a N-ary tree
- used to store strings (prefix)
- the corresponding relationship between characters and children nodes

## How to store children nodes
1. Array

```Python
class TrieNode:
  def __init__(self):
    self.N = 26
    self.children = [ ]
```

- Good
  - fast to visit a child node
  - easy to visit a specific child
 
- Bad
  - some waste of space

2. Hash Map

```python
class TrieNode:
  def __init__(self):
    children = { }  # key : character, value : corresponding child node
```

- Good
  - easier to visit a specific child directly
  - save some space
  - more flexible
- Bad
  - little slower than using an array  
