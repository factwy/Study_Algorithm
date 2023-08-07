# 2. Add Two Numbers
# Medium
# Time complexity : O(max(M, N)), Space complexity : O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = cur = ListNode()
        cur1, cur2 = l1, l2
        
        while cur1 or cur2:
            sum = 0
            if cur1 and cur2:
                sum = cur1.val + cur2.val
            elif cur1:
                sum = cur1.val
            else:
                sum = cur2.val
            
            next_val = (cur.val + sum) // 10
            cur.val = (cur.val + sum) % 10
            
            if (cur1 and cur1.next) or (cur2 and cur2.next) or next_val:
                cur.next = ListNode(next_val)
            
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
            cur = cur.next
            
        return res
