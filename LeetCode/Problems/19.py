# NeetCode - Linked List
# 19. Remove Nth Node From End of List
# Difficulty : Medium
# Algorithm : Linked List
# Time complexity : O(N), Space complexity : O(1)
# Runtime : 41 ms (84.49%), Memory : 16.3 MB (38.34%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # 1. count size of head
        slow, fast, cnt = head, head, 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            cnt += 1

        cnt = cnt * 2
        if fast:
            # if size of head is odd
            cnt += 1

        # 2. traverse into Nth Node
        cur = head
        prev, next = None, cur.next

        for _ in range(cnt - n):
            prev, cur = cur, next
            next = cur.next

        # 3. remove Nth Node
        if prev:
            prev.next = next
        else:
            return next

        return head
