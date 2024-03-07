/*
21. Merge Two Sorted Lists
Difficulty : Easy
Algorithm : Linked List
Time complexity : O(N), Space complexity : O(1)
Runtime : 0 ms (100%), Memory : 42.22 MB (75.56%)
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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if(list1 == null && list2 == null) {return null;}

        ListNode list = null;
        ListNode cur = null;

        while(list1 != null && list2 != null) {
            if(list1.val < list2.val) {
                if(list == null) {
                    list = new ListNode(list1.val);
                    cur = list;
                }
                else {
                    cur.next = new ListNode(list1.val);
                    cur = cur.next;
                }
                list1 = list1.next;
            }
            else {
                if(list == null) {
                    list = new ListNode(list2.val);
                    cur = list;
                }
                else {
                    cur.next = new ListNode(list2.val);
                    cur = cur.next;
                }
                list2 = list2.next;
            }
        }

        if(list1 != null) {
            if(list == null) {list = list1;}
            else {cur.next = list1;}
        }
        else if(list2 != null) {
            if(list == null) {list = list2;}
            else {cur.next = list2;}
        }

        return list;
    }
}
