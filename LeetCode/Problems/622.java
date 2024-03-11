/*
622. Design Circular Queue
Difficulty : Medium
Algorithm : Linked List, Queue
Time complexity : O(N), Space complexity : O(N)
Runtime : 4 ms (100%), Memory : 44.27 MB (92.45%)
*/

class MyCircularQueue {
    int[] queue;
    int head, tail, size, size_now;

    public MyCircularQueue(int k) {
        queue = new int[k];
        head = 0;
        tail = 0;
        size = k;
        size_now = 0;
    }   
    
    public boolean enQueue(int value) {
        if(isFull() == true) {return false;}
        queue[tail] = value;
        tail = (tail + 1) % size;
        size_now += 1;
        return true;
    }
    
    public boolean deQueue() {
        if(isEmpty() == true) {return false;}
        head += 1;
        head %= size;
        size_now -= 1;
        return true;
    }
    
    public int Front() {
        if(isEmpty() == true) {return -1;}
        return queue[head];
    }
    
    public int Rear() {
        if(isEmpty() == true) {return -1;}
        int n = (tail > 0) ? tail-1 : size-1;
        return queue[n];
    }
    
    public boolean isEmpty() {
        if(size_now == 0) return true;
        return false;
    }
    
    public boolean isFull() {
        if(size_now == size) return true;
        return false;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */
