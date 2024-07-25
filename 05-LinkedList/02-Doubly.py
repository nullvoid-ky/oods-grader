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
        if pos < 0:
            pos = self.size() + pos
        if pos < 0:
            pos = 0
        if pos == 0 or self.head == None:
            self.add_head(item)
        elif pos >= self.size():
            self.append(item)
        else:
            node = Node(item)
            cur = self.head
            for i in range(pos - 1):
                cur = cur.next
            node.next = cur.next
            node.pre = cur
            if cur.next:
                cur.next.pre = node
            cur.next = node
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
    while i[0] == " ":
        i = i[1:]
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
