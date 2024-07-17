
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

inp = input("Enter people and time : ").split(" ")
a, b = inp
lst = list(a)

q = Queue(lst)
q1 = Queue()
q2 = Queue()
b = int(b)
for i in range(b):
    if not q1.is_empty() and not i%3:
        q1.pop()
    if not q2.is_empty() and  i%2:
        q2.pop()
    if q1.size() < 5 and not q.is_empty():
        out = q.pop()
        q1.enqueue(out)
    elif q2.size() < 5 and not q.is_empty():
        out = q.pop()
        q2.enqueue(out)
    print(f"{i+1} {q} {q1} {q2}")



    # print(f"\n+++{i} \n{q}\n{q1}\n{q2}+++\n")
