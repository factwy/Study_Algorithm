# NeetCode - Linked List
# 141. Linked List Cycle
# Difficulty : Easy
# Algorithm : Linked List
# Time complexity : O(N), Space complexity : O(1)
# Runtime : 56 ms (90.60%), Memory : 20.30 MB (76.27%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False
