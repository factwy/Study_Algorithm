# NeetCode - Linked List
# 21. Merge Two Sorted Lists
# Difficulty : Easy
# Algorithm : Linked List
# Time complexity : O(N+M), Space complexity : O(N+M)
# Runtime : 57 ms (31.76%), Memory : 16.45 MB (14.92%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Time complexity : O(N+M), Space complexity : O(N+M)
        def rec(self, list1, list2):
            tmp = ListNode()

            if list1 and list2:
                if list1.val < list2.val:
                    tmp.val = list1.val
                    list1 = list1.next
                else:
                    tmp.val = list2.val
                    list2 = list2.next
            elif list1:
                tmp.val = list1.val
                list1 = list1.next
            elif list2:
                tmp.val = list2.val
                list2 = list2.next
            else:
                return

            node = tmp
            node.next = rec(self, list1, list2)
            return node

        return rec(self, list1, list2)
