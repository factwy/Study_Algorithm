/*
19. Remove Nth Node From End of List
Difficulty : Medium
Algorithm : Linked List, Two Pointers
Runtime : 0 ms (100%), Memory : 40.92 MB (99.02%)
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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode slow = head;
        ListNode fast = head;
        int cnt = 0;

        while(fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            cnt += 1;
        }
        cnt *= 2;
        if(fast != null) { cnt += 1;}

        if(cnt == n) { return head.next;}
        ListNode cur = head;
        for(int i=0; i<(cnt-n-1); i++) { cur = cur.next; }
        cur.next = cur.next.next;

        return head;
    }
}
