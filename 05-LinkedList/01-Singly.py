'''
 * กลุ่มที่  : 24010116
 * 66010056 กันต์ พัฒนาประทีปกุล
 * chapter : 5	item : 1	ครั้งที่ : 0003
 * Assigned : Thursday 18th of July 2024 09:19:44 AM --> Submission : Thursday 25th of July 2024 09:50:37 AM	
 * Elapsed time : 10110 minutes.
 * filename : 01-Singly.py
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.is_empty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def is_empty(self):
        return self.head == None

    def append(self, item):
        # Code Here
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
        else:
            cur = self.head
            while cur.next!= None:
                cur = cur.next
            cur.next = new_node

    def add_head(self, item):
        # Code Here
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def search(self, item):
        # Code Here
        cur = self.head
        while cur!= None:
            if cur.value == item:
                return True
            cur = cur.next
        return False

    def index(self, item):
        # Code Here
        cur = self.head
        index = 0
        while cur!= None:
            if cur.value == item:
                return index
            cur = cur.next
            index += 1
        return -1

    def size(self):
        # Code Here
        count = 0
        cur = self.head
        while cur!= None:
            count += 1
            cur = cur.next
        return count

    def pop(self, pos):
        if self.is_empty() or pos < 0 or pos >= self.size():
            return None
        if pos == 0:
            removed_value = self.head.value
            self.head = self.head.next
            return removed_value
        cur = self.head
        for _ in range(pos-1):
            cur = cur.next
        removed_value = cur.next.value
        cur.next = cur.next.next
        return removed_value


'''
1. append   ->  AP
2. addHead  ->  AH
3. search   ->  SE
4. index    ->  ID
5. size     ->  SI
6. pop      ->  PO
'''
L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.add_head(i[3:])
    elif i[:2] == "SE":
        itm = i[3:]
        fnd = ("Found" if L.search(itm) else "Not Found")
        print(f"{fnd} {itm} in {L}")
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = f"{L}"
        k = L.pop(int(i[3:]))
        if not k == None:
            k = "Success"
        # k = "Out of range" if None else "Success"
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else(f"{'Out of Range' if k == None else 'Success'} | {L}"))
print("Linked List :", L)


"""
Index (1) = -1 : Empty
Index (WOW) = -1 : Empty
Index (1) = -1 : WOW KMITL 
Index (WOW) = 0 : WOW KMITL 
Linked List : WOW KMITL 

Index (1) = -1 : Empty
Index (WOW) = -1 : Empty
Index (1) = -1 : WOW KMITL 
Index (WOW) = 0 : WOW KMITL 
Linked List : WOW KMITL 
"""