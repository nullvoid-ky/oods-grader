'''
 * กลุ่มที่  : 24010116
 * 66010056 กันต์ พัฒนาประทีปกุล
 * chapter : 5	item : 2	ครั้งที่ : 0010
 * Assigned : Thursday 18th of July 2024 09:28:30 AM --> Submission : Thursday 25th of July 2024 11:54:16 AM	
 * Elapsed time : 10225 minutes.
 * filename : 02-Doubly.py
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.pre = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self):
        if self.is_empty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next is not None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s.strip()
    
    def reverse(self):
        if self.is_empty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.pre is not None:
            s += str(cur.pre.value) + " "
            cur = cur.pre
        return s.strip()
    
    def is_empty(self):
        return self.head is None
    
    def append(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.pre = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def add_head(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.pre = new_node
            self.head = new_node
    
    def insert(self, pos, item):
        size = self.size()
        is_pos = False
        if pos < 0:
            is_pos = True
            self.reverse_list()
            pos = abs(pos)
        
        if size == 0:
            self.add_head(item)
            return
        
        if pos >= size:
            pos = pos % (size+1)
        
        new_node = Node(item)
        if pos == 0:
            self.add_head(item)
        elif pos == size:
            self.append(item)
        else:
            cur = self.head
            for _ in range(pos):
                cur = cur.next
            new_node.next = cur
            new_node.pre = cur.pre
            cur.pre.next = new_node
            cur.pre = new_node
        
        if is_pos:
            self.reverse_list()
    
    def reverse_list(self):
        cur = self.head
        self.head, self.tail = self.tail, self.head
        while cur:
            cur.pre, cur.next = cur.next, cur.pre
            cur = cur.pre
    
    def search(self, item):
        cur = self.head
        while cur is not None:
            if cur.value == item:
                return "Found"
            cur = cur.next
        return "Not Found"
    
    def index(self, item):
        cur = self.head
        idx = 0
        while cur is not None:
            if cur.value == item:
                return idx
            cur = cur.next
            idx += 1
        return -1
    
    def size(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count
    
    def pop(self, pos):
        if self.is_empty() or pos < 0 or pos >= self.size():
            return "Out of Range"
        if pos == 0:
            pop_value = self.head.value
            if self.head.next is not None:
                self.head = self.head.next
                self.head.pre = None
            else:
                self.head = None
                self.tail = None
            return "Success"
        elif pos == self.size() - 1:
            pop_value = self.tail.value
            self.tail = self.tail.pre
            self.tail.next = None
            return "Success"
        else:
            cur = self.head
            for _ in range(pos):
                cur = cur.next
            pop_value = cur.value
            cur.pre.next = cur.next
            cur.next.pre = cur.pre
            return "Success"

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.add_head(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1} -> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())
