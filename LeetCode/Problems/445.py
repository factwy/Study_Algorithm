# Daily challenge in 2023.07.17
# 445. Add Two Numbers II
# Difficulty : Medium
# Algorithm : Stack
# Time complexity : O(N), Space complexity : O(N) - N : max(len(l1), len(l2))
# Runtime : 84 ms (49.97%), Memory : 16.47 MB (31.76%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # ListNode -> Stack
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        # Sum of two numbers in stack -> ListNode
        res = None
        while stack1 or stack2:
            num = 0
            if stack1:
                num += stack1.pop()
            if stack2:
                num += stack2.pop()
            if num >= 10:
                if stack1:
                    stack1[-1] += 1
                else:
                    stack1.append(1)
                num -= 10

            node = ListNode(num)
            node.next = res
            res = node

        return res
