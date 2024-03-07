/*
328. Odd Even Linked List
Difficulty : Medium
Algorithm : Linked List
Runtime : 0 ms (100%), Memory : 44.02 MB (93.94%)
Time Complexity : O(N) , Space complexity : O(1)
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
    public ListNode oddEvenList(ListNode head) {
        if(head == null) { return head; }

        ListNode cur = head;
        ListNode new_head = null;
        ListNode new_head_cur = null;

        while(cur.next != null) {
            if(new_head == null) {
                new_head = new ListNode(cur.next.val);
                new_head_cur = new_head;
            } else { 
                new_head_cur.next = new ListNode(cur.next.val);
                new_head_cur = new_head_cur.next;
            }
            
            if(cur.next.next == null) { break; }
            cur.next = cur.next.next;
            cur = cur.next;
        }

        cur.next = new_head;
        return head;
    }
}
