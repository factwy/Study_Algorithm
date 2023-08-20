# NeetCode - Linked List
# 25. Reverse Nodes in k-Group
# Difficulty : Hard
# Algorithm : Linked List
# Time complexity : O(N), Space complexity : O(N)
# Runtime : 61 ms (49.16%), Memory : 18.1 MB (7.69%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, node):
        # reverse ListNode -> return [rev_node, tail]
        tail = node
        cur = node
        prev, next = None, cur.next

        while cur:
            cur.next = prev
            cur, prev = next, cur
            next = cur.next if cur else None

        return [prev, tail]

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # devide lists into k lists - Time complexity : O(N), Space complexity : O(N)
        divide, cnt = [], 0
        dummy = dum_cur = ListNode()
        cur = head

        while cur:
            dum_cur.next = ListNode(cur.val)
            dum_cur, cur = dum_cur.next, cur.next
            cnt += 1

            if cnt == k:
                divide.append(dummy.next)
                dummy = dum_cur = ListNode()
                cnt = 0

        # reverse each lists - Time complexity : O(N)
        for i in range(len(divide)):
            divide[i] = self.reverse(divide[i])

        # merge each lists - Time complexity : O(N/K)
        for i in range(len(divide)-1):
            divide[i][1].next = divide[i+1][0]
        divide[-1][1].next = dummy.next # if cnt < k -> not reverse

        return divide[0][0]
