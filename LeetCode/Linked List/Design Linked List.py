# Reference  NeetCode
# 707. Design Linked List
# Medium
# Runtime : 166 ms (79.29%), Memory : 17.82 mb (30.22%)
class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index == 0:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        node, prev, next = ListNode(val), self.left, self.left.next
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next

    def addAtTail(self, val: int) -> None:
        node, prev, next = ListNode(val), self.right.prev, self.right
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        while cur and index:
            cur = cur.next
            index -= 1
        if cur and index == 0:
            node, prev, next = ListNode(val), cur.prev, cur
            prev.next = node
            next.prev = node
            node.prev = prev
            node.next = next

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index:
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index == 0:
            prev, next = cur.prev, cur.next
            prev.next = next
            next.prev = prev
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
