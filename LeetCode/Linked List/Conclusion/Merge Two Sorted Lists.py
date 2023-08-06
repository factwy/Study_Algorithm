# 21. Merge Two Sorted Lists
# Easy
# Time complexity : O(N), Space complexity : O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if list1 is empty or list2 is empty
        if not list1 or not list2:
            return list1 if list1 else list2
        
        # start val : always list1 is bigger than or same list2
        if list1.val < list2.val:
            list1, list2 = list2, list1
        
        # list1 -> list2
        cur = list2
        while cur and list1:
            next = cur.next
            
            if list1.val >= cur.val:
                if next and next.val < list1.val:
                    cur = cur.next
                    continue
                # if next is None or cur.val <= list1.val <= next.val -> add node(list1)
                node = ListNode(list1.val)
                cur.next = node
                node.next = next
                list1 = list1.next
                
            cur = cur.next
        
        # if cur is list2's tail and list1 is not None -> cur.next = list1
        if list1:
            cur.next = list1
            
        return list2
