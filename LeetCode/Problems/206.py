# NeetCode - Linked List
# 206. Reverse Linked List
# Difficulty : Easy
# Algorithm : Linked List
# Time complexity : O(N), Space complexity : O(N)
# Runtime : 48 ms (80.36%), Memory : 18.52 MB (20.01%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        
        while head:
            linked = ListNode()
            linked.next = res
            linked.val = head.val

            res = linked
            head = head.next

        return res
