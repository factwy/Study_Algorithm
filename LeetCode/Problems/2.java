/*
2. Add Two Numbers
Difficulty : Medium
Algorithm : Linked List
Time complexity : O(N), Space complexity : O(1)
Runtime : 1 ms (100%), Memory : 44.10 MB (91.86%)
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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode cur1 = l1;
        ListNode cur2 = l2;

        int isupper = 0;
        while(cur1.next != null && cur2.next != null) {
            cur1.val += (cur2.val + isupper);
            isupper = 0;
            if(cur1.val >= 10) {
                isupper += 1;
                cur1.val -= 10;
            }
            cur1 = cur1.next;
            cur2 = cur2.next;
        }

        cur1.val += (cur2.val + isupper);
        isupper = 0;
        if(cur1.val >= 10) {
            isupper = 1;
            cur1.val -= 10;
        }

        if(cur2.next == null && cur1.next == null) 
            {if(isupper > 0) {cur1.next = new ListNode(1);}}
        else if(cur2.next == null) {
            while(isupper == 1) {
                if(cur1.next == null) {
                    cur1.next = new ListNode(1);
                    break;
                }
                cur1.next.val += isupper;
                isupper = 0;
                if(cur1.next.val >= 10) {
                    isupper = 1;
                    cur1.next.val -= 10;
                    cur1 = cur1.next;
                }
            }
        }
        else {
            cur1.next = cur2.next;
            while(isupper == 1) {
                if(cur1.next == null) {
                    cur1.next = new ListNode(1);
                    break;
                }
                cur1.next.val += isupper;
                isupper = 0;
                if(cur1.next.val >= 10) {
                    isupper = 1;
                    cur1.next.val -= 10;
                    cur1 = cur1.next;
                    }
                }
            }

            return l1;
        }
}
