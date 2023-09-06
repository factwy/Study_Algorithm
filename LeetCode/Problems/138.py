# NeetCode - Linked List
# 138. Copy List with Random Pointer
# Difficulty : Medium
# Algorithm : Linked List
# Time complexity : O(N), Space complexity : O(N)
# Runtime : 42 ms (74.35%), Memory : 17.26 MB (70.34%)

# Refernce Neetcode Solution

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_map = { None : None }  # if node.next of node.random is None -> return None

        # 1. create copy and store
        cur = head
        while cur:
            hash_map[cur] = Node(cur.val)
            cur = cur.next

        # 2. connect each copy using hash_map and original
        cur = head
        while cur:
            node = hash_map[cur]
            node.next = hash_map[cur.next]
            node.random = hash_map[cur.random]
            cur = cur.next

        # 3. return
        return hash_map[head]
