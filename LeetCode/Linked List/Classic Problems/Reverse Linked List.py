# 206. Reverse Linked List
# Easy
# Runtime : 41 ms (93.96%), Memory : 18.7 mb (16.32%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        res = ListNode(head.val)
        head = head.next
        
        while head:
            node = ListNode(head.val)
            node.next = res
            res = node
            
            head = head.next
            
        return res
