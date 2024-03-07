/*
61. Rotate List
Difficulty : Medium
Algorithm : Linked List
Time complexity : O(N), Space complexity : O(1)
Runtime : 0 ms (100%), Memory : 42..44 MB (51.73%)
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if(head == null) {return head;}
        if(head.next == null) {return head;}

        ListNode slow = head, fast = head;
        int cnt = 0;
        while(fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            cnt += 1;
        }
        cnt *= 2;
        if(fast != null) {cnt += 1;}

        k %= cnt;
        for(int i=0; i<k; i++) {head = rotate(head);}
        return head;
    }

    public ListNode rotate(ListNode node) {
        if(node == null) {return node;}
        if(node.next == null) {return node;}
        if(node.next.next == null) {
            node.next.next = new ListNode(node.val);
            node = node.next;
            return node;
        }

        ListNode cur = node;
        while(cur.next.next != null) {cur = cur.next;}
        ListNode tail = cur.next;
        tail.next = node;
        cur.next = null;
        return tail;
    }
}
