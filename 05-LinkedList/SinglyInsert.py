
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
    
    def insert(self, pos, item):
        new_node = Node(item)
        if pos < 0 or pos > self.size():
            return None
        elif pos == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            cur = self.head
            for _ in range(pos - 1):
                cur = cur.next
            new_node.next = cur.next
            cur.next = new_node
        return "Success"
    def print_pattern(self):
        if self.head is None:
            print("List is empty")
        else:
            print(f"link list : {self.head.value}", end="")
            cur = self.head.next
            while cur:
                print(f"->{cur.value}", end='')
                cur = cur.next
            print()
'''
1. append   ->  AP
2. addHead  ->  AH
3. search   ->  SE
4. index    ->  ID
5. size     ->  SI
6. pop      ->  PO
'''
# 1 2, 0:0, 3:3
L = LinkedList()
inp = input('Enter Input : ')
(mylist, operation) = (inp.split(',',1)) if not inp[0] == "," else (None , inp[1:])
if not mylist == None:
    for i in mylist.split():
        L.append(i)
L.print_pattern()
for i in operation.split(','):
    idx , value = i.split(":")
    while idx[0] == " ":
        idx = idx[1:]
    a = L.insert(int(idx), value)
    if a == "Success":
        print(f"index = {idx} and data = {value}")
    else :
        print("Data cannot be added")
    L.print_pattern()
