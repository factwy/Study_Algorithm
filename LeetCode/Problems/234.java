/*
234. Palindrome Linked List
Difficulty : Easy
Algorithm : Linked List
Runtime : 5 ms (61.38%), Memory : 57.32 MB (88.11%)
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
    public boolean isPalindrome(ListNode head) {
        if(head.next == null) { return true; }

        ListNode slow = head;
        ListNode fast = head;
        while(fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        if(fast != null) { slow = slow.next; }

        ListNode cur = slow;
        while(cur.next != null) {
            ListNode node = new ListNode(cur.next.val);
            cur.next = cur.next.next;
            node.next = slow;
            slow = node;
        }

        while(slow != null) {
            if(slow.val != head.val) { return false; }
            slow = slow.next;
            head = head.next;
        }
        return true;
    }
}
