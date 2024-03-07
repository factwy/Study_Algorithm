/*
707. Design Linked List
Difficulty : Medium
Algorithm : Linked List
Time complexity : O(N), Space complexity : O(1)
Runtime : 6 ms (99.11%), Memory : 45.28 MB (81.08%)
- Doubly Linked List
*/

class DoublyListNode {
    int val;
    DoublyListNode prev, next;
    DoublyListNode(int x) {val = x;}
}

class MyLinkedList {
    DoublyListNode head;
    DoublyListNode tail;
    DoublyListNode cur;
    int size;

    public MyLinkedList() {
        head = null;
        tail = null;
        cur = null;
        size = 0;
    }
    
    public int get(int index) {
        if(index >= size) {return -1;}

        DoublyListNode cur = head;
        for(int i=0; i<index; i++) {cur = cur.next;}
        return cur.val;
    }
    
    public void addAtHead(int val) {
        DoublyListNode node = new DoublyListNode(val);

        if(head == null) {
            head = node;
            tail = node;
            cur = node;
        } else {
            node.next = head;
            head.prev = node;
            head = node;
        }
        size += 1;
    }
    
    public void addAtTail(int val) {
        DoublyListNode node = new DoublyListNode(val);

        if(tail == null) {
            head = node;
            tail = node;
            cur = node;    
        } else {
            tail.next = node;
            node.prev = tail;
            tail = node;
        }
        size += 1;
    }
    
    public void addAtIndex(int index, int val) {
        if(index == 0) {addAtHead(val);}
        else if(index == size) {addAtTail(val);}
        else if(index > size) {return;}
        else {
            DoublyListNode node = new DoublyListNode(val);
            DoublyListNode cur = head;

            for(int i=0; i<(index-1); i++) {cur = cur.next;}
            DoublyListNode next = cur.next;
            node.prev = cur;
            node.next = next;
            cur.next = node;
            next.prev = node;
            size += 1;
        }
    }
    
    public void deleteAtIndex(int index) {
        if(size == 0 || index >= size) {return;}
        if(size == 1 && index == 0) {
            head = null;
            tail = null;
            cur = null;
            size = 0;
        }
        else if(index == 0) {
            DoublyListNode node = head.next;
            node.prev = null;
            head = node;
        }
        else if(index == size-1) {
            DoublyListNode node = tail.prev;
            node.next = null;
            tail = node;
        }
        else {
            DoublyListNode node = head;
            for(int i=0; i<index; i++) {node = node.next;}
            DoublyListNode prev = node.prev;
            DoublyListNode next = node.next;
            
            prev.next = next;
            next.prev = prev;
        }
        size -= 1;
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */
