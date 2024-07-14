class Queue:
    def __init__(self, lst : list = None):
        self.items = lst if lst != None else []
        self.size = len(self.items)
    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.items[0] if self.size > 0 else None
    def push(self, item):
        self.items.append(item)
        self.size += 1
    def top(self):
        return self.items[-1] if self.size > 0 else None
    def __str__(self):
        return str(self.items)
    def is_empty(self):
        return self.size == 0
    def clear(self):
        self.items = []
        self.size = 0
    def reverse(self):
        self.items = self.items[::-1]
    def has(self, item):
        return item == self.items
    def index(self, item):
        return self.items.index(item) if item in self.items else -1
    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
            self.size -= 1
    def sort(self):
        self.items.sort()
    def dequeue(self):
        return self.pop()
    def enqueue(self, item):
        self.push(item)
    def peek(self):
        return self.top()
    def size(self):
        return self.size
    def front(self):
        return self.items[0] if self.size > 0 else None

