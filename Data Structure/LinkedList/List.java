//*************************************************
// Author: Alireza Nikian
// Faculty of Computer Engineering
// Islamic Azad University, Najafabad Branch
//
// class List
//*************************************************

public class List { // IntLinkedList
    private ListNode first;
    private int size;

    public List() {
        first = null;
        size = 0;
    }

    public boolean isEmpty() {
        if (first == null)
            return true;
        return false;
    }

    public int size() {
        return size;
    }

    private void checkIndex(int index, int size) {
        if (!(index >= 0 && index < size))
            throw new IndexOutOfBoundsException("index=" + index + " size=" + size);

    }

    public int get(int index) {
        checkIndex(index, size);
        ListNode p = first;
        for (int i = 0; i < index; i++)
            p = p.next;
        return p.data;
    }

    public int set(int index, int item) {
        checkIndex(index, size);
        ListNode p = first;
        for (int i = 0; i < index; i++)
            p = p.next;
        int value = p.data;
        p.data = item;
        return value;
    }

    // ***********************************************************
    public void addFirst(int item) {
        ListNode temp = new ListNode(item);
        temp.next = first;
        first = temp;
        size++;
    }

    public void addLast(int item) {
        ListNode temp = new ListNode(item);
        if (first == null)
            first = temp;
        else {
            ListNode p;
            for (p = first; p.next != null; p = p.next)
                ; // do nothing
            p.next = temp;
        }
        size++;
    }

    public void add(int item) {
        addLast(item); // add(size,item);
    }

    public void add(int index, int item) {
        checkIndex(index, size + 1);
        ListNode temp = new ListNode(item);
        if (index == 0) {
            temp.next = first;
            first = temp;
        } else {
            ListNode p = first;
            for (int i = 1; i < index; i++)
                p = p.next;
            temp.next = p.next;
            p.next = temp;
        }
        size++;
    }

    public static List readList() {
        List lst = new List();
        java.util.Scanner input = new java.util.Scanner(System.in);
        System.out.print("Enter an integer number, negative or zero to quit: ");
        int n = input.nextInt();
        while (n > 0) {
            lst.addLast(n);
            System.out.print("Enter an integer number, negative or zero to quit: ");
            n = input.nextInt();
        }
        input.close();
        return lst;
    }

    public static List createList(int... args) {
        List lst = new List();
        for (int i = 0; i < args.length; i++)
            lst.addLast(args[i]);
        return lst;
    }

    // ***********************************************************
    public int removeFirst() throws EmptyListException {
        if (isEmpty())
            throw new EmptyListException("list is empty");
        int item = first.data;
        first = first.next;
        size--;
        return item;
    }

    public int removeLast() throws EmptyListException {
        if (isEmpty())
            throw new EmptyListException("list is empty");
        int item;
        if (first.next == null) {
            item = first.data;
            first = null;
        } else {
            ListNode p = first;
            while (p.next.next != null)
                p = p.next;
            item = p.next.data;
            p.next = null;
        }
        size--;
        return item;
    }


    public int remove(int index) throws EmptyListException {
        checkIndex(index, size);
        if (isEmpty())
            throw new EmptyListException("list is empty");
        if (index == 0)
            return removeFirst();
        ListNode p = first;
        for (int i = 1; i < index; i++)
            p = p.next;
        int item = p.next.data;
        p.next = p.next.next;
        size--;
        return item;
    }

    // ***********************************************************
    public void printList() {
        // System.out.println("The linked list contains:");
        for (ListNode p = first; p != null; p = p.next)
            System.out.print(p.data + " ");
        System.out.println();
    }

    public void recursivePrintList() {
        printList(first);
    }

    private void printList(ListNode p) { // Recursive
        if (p != null) {
            System.out.print(p.data + " ");
            printList(p.next);
        }
    }

    @Override
    public String toString() {
        String s = "[";
        ListNode p = first;
        while (p != null) {
            s += p.data;
            if (p.next != null)
                s += ", ";
            p = p.next;
        }
        s += "]";
        return s;
    }

    public boolean contains(int item) {
        ListNode p = first;
        while (p != null) {
            if (p.data == item)
                return true;
            p = p.next;
        }
        return false; // not found
    }

    public int indexOf(int item) {
        ListNode p = first;
        int i = 0;
        while (p != null) {
            if (p.data == item)
                return i;
            p = p.next;
            i++;
        }
        return -1; // not found
    }

    // **********************************************************
    public void concat(List other) {
        if (first == null)
            first = other.first;
        else if (other.first != null) {
            ListNode p;
            for (p = first; p.next != null; p = p.next)
                ; // do nothing
            p.next = other.first;
        }
        size += other.size;
    }

    public List invertList() {
        ListNode p = first;
        ListNode q = null; // q trails p
        ListNode r;
        while (p != null) {
            r = q;
            q = p;
            p = p.next; // p moves to next node
            q.next = r; // link q to preceding node
        }
        first = q;
        return this;
    }
    // ---------------------------------------------------------------
    //                          NEW METHODS 
    
    public int indexOf(ListNode item) {
        int index = 0;
        ListNode p = first;
        for (; index < size; index++) {
            if (p == item) {
                break;
            }
        }

        return index;
    }

    public int removeMax() throws EmptyListException { // added by siavash
        if (isEmpty())
            throw new EmptyListException("list is empty");
        ListNode p = first;
        ListNode max = p;
        
        while(p.next != null){
            if (max.data < p.next.data){
                max = p.next;
            }
            p = p.next;
        }
        int index = indexOf(max);
        remove(index);
        return max.data;
    }

    public int removeMin() throws EmptyListException { // added by siavash
        if (isEmpty())
            throw new EmptyListException("list is empty");
        ListNode p = first;
        ListNode min = p;
        
        while(p.next != null){
            if (min.data > p.next.data){
                min = p.next;
            }
            p = p.next;
        }
        int index = indexOf(min);
        remove(index);
        return min.data;
    }


    public boolean equals(List anotherList) throws EmptyListException {
        if(size != anotherList.size){
            return false;
        }
        ListNode a = first;
        ListNode b = anotherList.first;
        for(int i=0; i<size; i++){
            if(a.data != b.data){
                return false;
            }
            else{
                a = a.next;
                b = b.next;
            }
        }
        return true;
    }

    /////////////////////////////////////////////////////////////
    public int sum() {
        return sum(first);
    }

    private int sum(ListNode p) { // Recursive
        if (p == null)
            return 0;
        return p.data + sum(p.next);
    }

    public void test() {
        test(first);
    }

    private void test(ListNode p) { // Recursive
        if (p != null) {
            test(p.next);
            System.out.print(p.data + " ");
            test(p.next);
            System.out.print(p.data + " ");
        }
    }

}