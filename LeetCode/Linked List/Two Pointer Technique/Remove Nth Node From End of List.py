# 19. Remove Nth Node From End of List
# Medium
# Time complexity : O(N), Space complexity : O(1)
# Runtime : 49 ms (59.51%), Memory : (74.10%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, cur, end = None, head, head
        for _ in range(n-1):
            end = end.next
            
        while end and end.next:
            end = end.next
            cur = cur.next
            prev = prev.next if prev else head
            
        if prev:
            prev.next = cur.next
        else:
            head = head.next
        
        return head
