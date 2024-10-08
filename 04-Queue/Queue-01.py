
class Queue:
    def __init__(self, lst=None):
        self.items = lst if lst is not None else []

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def push(self, item):
        self.items.append(item)

    def top(self):
        return self.items[0] if not self.is_empty() else None

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def clear(self):
        self.items = []

    def reverse(self):
        self.items.reverse()

    def has(self, item):
        return item in self.items

    def index(self, item):
        return self.items.index(item) if item in self.items else -1

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)

    def sort(self):
        self.items.sort()

    def dequeue(self):
        return self.pop()

    def enqueue(self, item):
        self.push(item)

    def peek(self):
        return self.top()

    def size(self):
        return len(self.items)

    def front(self):
        return self.top()

# Input processing
q = Queue()
q2 = Queue()
inp = input("Enter Input : ").split(",")
for item in inp:
    if " " in item:
        a, b = item.split()
        b = int(b)
    else:
        a = item
    if a == "E":
        q.enqueue(b)
        txt = str(q.items)[1:-1]
        print(f"{txt}")
    elif a == "D":
        if q.size() >= 1:
            out = q.dequeue()
            q2.enqueue(out)
            txt = str(q.items)[1:-1]
            if q.size():
                if not q2.size():
                    print(f"Empty <- {txt}")
                else:
                    print(f"{out} <- {txt}")
            else:
                if not q2.size():
                    print(f"Empty  Empty")
                else:
                    print(f"{out} <- Empty")
        else:
            print(f"Empty")
       
txt1 = str(q2.items)[1:-1]
txt2 = str(q.items)[1:-1]
if q.size():
    if not q2.size():
        print(f"Empty : {txt}")
    else:
        print(f"{txt1} : {txt}")
else:
    if not q2.size():
        print(f"Empty : Empty")
    else:
        print(f"{txt1} : Empty")

