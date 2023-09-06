# Daily challenge in 2023.09.06
# 725. Split Linked List in Parts
# Difficulty : Medium
# Algorithm : Linkted List
# Time complexity : O(N+K), Space complexity : O(N)
# Runtime : 52 ms (27.93%), Memory : 17.03 MB (9.46%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # 1. count len(head)
        cnt = 0
        cur = head
        while cur:
            cnt += 1
            cur = cur.next

        # 2. split
        res = []
        if cnt >= k:
            num = cnt // k
            cur = head
            for i in range(k):
                node = node_cur = ListNode()
                if i < (cnt % k):
                    # size : num + 1
                    for _ in range(num+1):
                        node_cur.next = ListNode(cur.val)
                        node_cur = node_cur.next
                        cur = cur.next
                else:
                    # size : num
                    for _ in range(num):
                        node_cur.next = ListNode(cur.val)
                        node_cur = node_cur.next
                        cur = cur.next
                res.append(node.next)

        else:
            cur = head
            for _ in range(cnt):
                res.append(ListNode(cur.val))
                cur = cur.next
            for _ in range(k-cnt):
                res.append(None)

        return res
