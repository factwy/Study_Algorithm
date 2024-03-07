/*
203. Remove Linked List Elements
Difficulty : Easy
Algorithm : Linked List
Runtime : 1 ms (91.46%), Memory : 42.21 MB (69.84%)
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
    public ListNode removeElements(ListNode head, int val) {
        ListNode prev = null;
        ListNode cur = head;
        
        while(cur != null) {
            if(cur.val == val) {
                cur = cur.next;
                if(prev == null) { head = head.next; }
                else { prev.next = prev.next.next; }
            } else {
                cur = cur.next;
                if(prev == null) { prev = head; }
                else { prev = prev.next; }
            }
        }
        return head;
    }
}
