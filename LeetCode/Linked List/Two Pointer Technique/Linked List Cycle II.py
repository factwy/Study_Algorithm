# 142. Linked List Cycle II
# Medium
# Runtime : 44 ms (99.93%), Memory : 20.3 mb (90.26%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
                
        fast = head
        while fast.next and slow.next:
            if fast == slow:
                return fast
            
            fast = fast.next
            slow = slow.next
        return None
