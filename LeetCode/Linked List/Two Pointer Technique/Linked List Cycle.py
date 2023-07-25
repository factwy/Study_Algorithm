# 141. Linked List Cycle
# Easy
# Runtime : 79 ms (32.98%), Memory : 20.4 mb (62.50%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow, fast = head, head.next
        while fast and slow != fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            
        return slow == fast
