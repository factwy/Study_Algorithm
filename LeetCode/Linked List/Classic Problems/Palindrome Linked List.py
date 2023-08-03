# 234. Palindrome Linked List
# Easy
# Runtime : 901 ms (13.63%), Memory : 49.1 mb (37.30%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        half = None
        curr = slow
        while curr:
            node = ListNode(curr.val)
            node.next = half
            half = node
            
            curr = curr.next
            
        while half:
            if half.val != head.val:
                return False
            half, head = half.next, head.next
        
        return True
