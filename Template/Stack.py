class Stack:
    def __init__(self, lst : list = None):
        self.items = lst if lst != None else []
        self.size = len(self.items)
    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        self.items = self.items[:self.size]
        return self.items[-1] if self.size > 0 else None
    def push(self, item):
        self.items.append(item)
        self.size += 1
    def is_empty(self):
        return self.size == 0
    def peek(self):
        return self.items[-1] if self.size > 0 else None
    def __str__(self) -> str:
        return str(self.items)
    def clear(self):
        self.items = []
        self.size = 0
    def reverse(self):
        self.items = self.items[::-1]
    def has(self, item):
        return item in self.items
    def index(self, item):
        return self.items.index(item) if item in self.items else -1
    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
            self.size -= 1
    def sort(self):
        self.items.sort()
