# Daily challenge in 2023.09.07
# 92. Reverse Linked List II
# Difficulty : Medium
# Algorithm : Linkted List
# Time complexity : O(N), Space complexity : O(1)
# Runtime : 48 ms (20.17%), Memory : 16.62 MB (8.62%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # input :  head - [left ListNode ~ right ListNode] - tail
        # output : head = [right ListNode ~ left ListNode] - tail

        if left == right:
            return head

        # 1. find left ListNode
        cur, prev = head, None
        for _ in range(left-1):
            prev = prev.next if prev else head
            cur = cur.next
        head_tail = prev
        leftNode = cur

        # 2. find right ListNode
        for _ in range(right - left):
            cur = cur.next
        rightNode = cur

        tail = cur.next
        cur.next = None

        # 3. reverse
        cur, prev = leftNode, None
        while cur:
            next = cur.next
            cur.next = prev
            cur, prev = next, cur
        
        # 4. connect
        leftNode.next = tail
        if left == 1:
            return rightNode
        head_tail.next = rightNode
        return head
