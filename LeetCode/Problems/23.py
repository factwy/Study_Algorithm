# NeetCode - Linked List
# 23. Merge k Sorted Lists
# Difficulty : Hard
# Algorithm : Linked List
# Time complexity : O(NlogK), Space complexity : O(NK)
# Runtime : 150 ms (23.66%), Memory : 22.32 MB (5.68%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, l1, l2):
        cur = dummy = ListNode()
        l1_cur, l2_cur = l1, l2

        while l1_cur and l2_cur:
            if l1_cur.val < l2_cur.val:
                cur.next = ListNode(l1_cur.val)
                l1_cur = l1_cur.next
            else:
                cur.next = ListNode(l2_cur.val)
                l2_cur = l2_cur.next
            cur = cur.next

        if l1_cur:
            cur.next = l1_cur
        else:
            cur.next = l2_cur

        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        # merge 2 sorted lists

        lists = deque(lists)
        while len(lists) != 1:
            l1 = lists.popleft()
            l2 = lists.popleft() if lists else None

            lists.append(self.merge(l1, l2))

        return lists[0]
