/*
160. Intersection of Two Linked Lists
Difficulty : Easy
Algorithm : Linked List, Two Pointers
Runtime : 1 ms (99.92%), Memory : 47.05 MB (99.77%)
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int a_length = 0;
        int b_length = 0;
        ListNode head = headA;
        while(head != null) {
            a_length += 1;
            head = head.next;
        }
        head = headB;
        while(head != null) {
            b_length += 1;
            head = head.next;
        }

        while(headA != null && headB != null) {
            if(a_length == b_length && headA == headB) { return headA; }
            if(a_length > b_length) {
                headA = headA.next;
                a_length -= 1;
            }
            else {
                headB = headB.next;
                b_length -= 1;
            }
        }
        return null;
    }
}
