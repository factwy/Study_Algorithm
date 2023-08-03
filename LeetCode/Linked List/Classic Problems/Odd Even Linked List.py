# 328. Odd Even Linked List
# Medium
# Runtime : 46 ms (95.52%), Memory : 19 mb (16.49%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        even = ListNode()
        even_curr = even
        
        curr = head
        while True:
            even_curr.next = curr.next
            even_curr = even_curr.next
            
            next_odd = curr.next.next if curr.next else None
            curr.next = next_odd
            if next_odd:
                curr = next_odd
            else:
                break
            
        curr.next = even.next
        return head
