# Daily challenge in 2023.08.15
# 86. Partition List
# Difficulty : Medium
# Algorithm : Linked List
# Time complexity : O(N), Space complexity : O(1)
# Runtime : 41 ms (84.58%), Memory : 16.34 MB (55.72%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less, greater = ListNode(), ListNode()
        cur, l_cur, g_cur = head, less, greater

        while cur:
            if cur.val < x:
                l_cur.next = ListNode(cur.val)
                l_cur = l_cur.next
            else:
                g_cur.next = ListNode(cur.val)
                g_cur = g_cur.next
            cur = cur.next

        l_cur.next = greater.next
        return less.next
