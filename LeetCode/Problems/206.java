/*
206. Reverse Linked List
Difficulty : Easy
Algorithm : Linked List
Runtime : 0 ms (100%), Memory : 42.21 MB (69.84%)
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
    public ListNode reverseList(ListNode head) {
        ListNode cur = head;
        while(cur != null && cur.next != null) {
            ListNode node = cur.next;
            cur.next = cur.next.next;
            node.next = head;
            head = node;
        }
        return head;
    }
}
