/*
142. Linked List Cycle II
Difficulty : Medium
Algorithm : Linked List, Two Pointers
Runtime : 0 ms (100%), Memory : 44.36 MB (68.65%)
*/

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if(head == null) { return null; }
        else if(head.next == null) { return null; }
        ListNode slow = head.next;
        ListNode fast = head.next.next;

        while(slow != fast) {
            if(fast == null) { return null; }

            if(fast.next != null) {
                slow = slow.next;
                fast = fast.next.next;
            } else { return null; }
        }
        
        slow = head;
        while(slow != fast) {
            slow = slow.next;
            fast = fast.next;
        }
        return slow;
    }
}
