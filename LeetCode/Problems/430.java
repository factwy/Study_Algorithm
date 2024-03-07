/*
430. Flatten a Multilevel Doubly Linked List
Difficulty : Medium
Algorithm : Linked List
Time complexity : O(N), Space complexity : O(1)
Runtime : 0 ms (100%), Memory : 41.85 MB (24.49%)
*/

/*
// Definition for a Node.
class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;
};
*/

class Solution {
    public Node flatten(Node head) {
        if(head == null) {return head;}
        Node cur = head;
        cur = connect(cur);

        return head;
    }

    public Node connect(Node cur) {
        if(cur == null) {return null;}
        Node next = cur.next;
        Node child = cur.child;
        cur.child = null;

        if(child != null) {
            cur.next = child;
            child.prev = cur;
            cur = connect(child);
        }

        if(next != null) {
            cur.next = next;
            next.prev = cur;
            cur = connect(next);
        }

        return cur;
    }
}
