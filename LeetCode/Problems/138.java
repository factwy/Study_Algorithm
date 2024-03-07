/*
138. Copy List with Random Pointer
Difficulty : Medium
Algorithm : Linked List
Time complexity : O(N), Space complexity : O(1)
Runtime : 0 ms (100%), Memory : 44.14 MB (83.42%)
*/

/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

import java.util.*;

class Solution {
    public Node copyRandomList(Node head) {
        if(head == null) {return null;}
        Node node = new Node(head.val);
        Node cur = node;
        Node head_cur = head;

        Map<Node, Node> dict = new HashMap<>();
        dict.put(head_cur, cur);

        while(head_cur.next != null) {
            cur.next = new Node(head_cur.next.val);
            cur = cur.next;
            head_cur = head_cur.next;
            dict.put(head_cur, cur);
        }

        cur = node;
        head_cur = head;
        while(cur != null) {
            cur.random = dict.get(head_cur.random);
            cur = cur.next;
            head_cur = head_cur.next;
        }

        return node;
    }
}
