/*
707. Design Linked List
Difficulty : Medium
Algorithm : Linked List
Time complexity : O(N), Space complexity : O(1)
Runtime : 10 ms (20.55%), Memory : 45.74 MB (20.21%)
- Singly Linked List
*/

class MyLinkedList {
    int val;
    MyLinkedList next;
    MyLinkedList head;

    public MyLinkedList() {}
    
    public int get(int index) {
        MyLinkedList node = this.head;
        for(int i=0; i<index; i++) {
            if(node == null) { return -1; }
            node = node.next;
        }
        if(node == null) { return -1; }
        else { return node.val; }
    }
    
    public void addAtHead(int val) {
        MyLinkedList node = new MyLinkedList();
        node.val = val;

        node.next = this.head;
        this.head = node;
    }
    
    public void addAtTail(int val) {
        MyLinkedList node = new MyLinkedList();
        node.val = val;

        MyLinkedList cur = this.head;
        if(cur == null) { 
            this.head = node;
            return;
        }
        while(cur.next != null) { cur = cur.next; }
        cur.next = node;
    }
    
    public void addAtIndex(int index, int val) {
        MyLinkedList node = new MyLinkedList();
        node.val = val;

        if(index == 0) {
            node.next = this.head;
            this.head = node;
            return;
        }

        MyLinkedList cur = this.head;
        for(int i=0; i<(index-1); i++) {
            if(cur == null) { return; }
            cur = cur.next;
        }
        if(cur == null) { return; }
        node.next = cur.next;
        cur.next = node;
    }
    
    public void deleteAtIndex(int index) {
        if(this.head == null) { return; }

        if(index == 0) { 
            if(this.head.next == null) { this.head = null;}
            else { this.head = this.head.next; }
        }
        else {
            MyLinkedList cur = this.head;
            for(int i=0; i<(index-1); i++) {
                if(cur.next == null) { return; }
                cur = cur.next;
            }
            if(cur.next != null) { cur.next = cur.next.next; }
        }
    }
}
