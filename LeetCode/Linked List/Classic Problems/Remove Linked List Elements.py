# 203. Remove Linked List Elements
# Easy
# Runtime : 69 ms (92.72%), Memory : 19.8 mb (82.59%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        
        res = ListNode(-1, head)
        node, prev = head, res
        while node:
            next = node.next
            
            if node.val == val:
                prev.next = next
                node = next
            else:
                prev, node = node, next
                
        return res.next
