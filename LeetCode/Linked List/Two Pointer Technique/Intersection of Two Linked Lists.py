# 160. Intersection of Two Linked Lists
# Easy
# Time complexity : O(N+M), Space complexity : O(1)
# Runtime : 131 ms (100%), 31.6 mb (70.11%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        list1, list2 = headA, headB
        cross1, cross2 = False, False
        
        while True:
            if list1 == list2:
                return list1
            
            if list1.next:
                list1 = list1.next
            else:
                list1 = headA if cross1 else headB
                cross1 = not cross1
                    
            if list2.next:
                list2 = list2.next
            else:
                list2 = headB if cross2 else headA
                cross2 = not cross2
            
            if list1 == headA and list2 == headB:
                return None
