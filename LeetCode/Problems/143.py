# NeetCode - Linked List
# 143. Reorder List
# Difficulty : Medium
# Algorithm : Linked List
# Time complexity : O(N), Space complexity : O(1)
# Runtime : 88 ms (84.12%), Memory : 27.1 MB (5.15%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, listnode):
        cur = listnode
        prev, next = None, cur.next

        while cur:
            cur.next = prev
            prev, cur = cur, next
            next = next.next if next else None

        return prev
            

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 0. if len(head) == 1 -> finish
        if not head.next:
            return
            
        # 1. find mid -> using slow, fast
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            prev = prev.next if prev else head
        mid = slow

        if fast:
            mid = mid.next
            prev = prev.next if prev else None

        # 2. reverse ListNode
        ListNode2 = self.reverse(mid)
        ListNode1 = head
        if prev:
            prev.next = None

        # 3. Merge half ListNode1, reversed half ListNode2
        while ListNode2:
            node = ListNode(ListNode2.val, ListNode1.next)
            ListNode1.next = node

            ListNode2 = ListNode2.next
            ListNode1 = node.next
