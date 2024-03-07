/*
141. Linked List Cycle
Difficulty : Easy
Algorithm : Linked List, Two Pointers
Runtime : 0 ms (100%), Memory : 43.77 MB (98.31%)
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
    public boolean hasCycle(ListNode head) {
        if(head == null) { return false; }
        ListNode slow = head;
        ListNode fast = head.next;

        while(fast != null) {
            if(slow == fast) { return true; }

            if(fast.next != null) {
                slow = slow.next;
                fast = fast.next.next;
            } else { break; }
        }
        return false;
    }
}
