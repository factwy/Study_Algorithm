# NeetCode - Linked List
# 2. Add Two Numbers
# Difficulty : Medium
# Algorithm : Linked List
# Time complexity : O(N), Space complexity : O(1)
# Runtime : 64 ms (88.54%), Memory : 16.31 MB (66.20%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_cur, l2_cur = l1, l2
        res = res_cur = ListNode()
        last_num = 0

        while l1_cur or l2_cur:
            l1_val = l1_cur.val if l1_cur else 0
            l2_val = l2_cur.val if l2_cur else 0
            sum = l1_val + l2_val + last_num
            sum, last_num = sum%10, sum//10

            res_cur.next = ListNode(sum)

            res_cur = res_cur.next
            l1_cur = l1_cur.next if l1_cur else None
            l2_cur = l2_cur.next if l2_cur else None
        if last_num:
            res_cur.next = ListNode(last_num)

        return res.next
