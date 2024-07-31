class Stack:
    def __init__(self, items=None):
        if items == None:
            self.items = []
        else:
            self.items = items
    def size(self):
        if len(self.items) == 0:
            return None
        return len(self.items)
    def is_empty(self):
        return self.size() == None
    def __str__(self):
        return self.items
    def push(self, item):
        self.items.append(item)
    def peek(self):
        if self.is_empty():
            return None
        item = self.items[self.size() - 1]
        return item
    def pop(self):
        if self.is_empty():
            return None
        item = self.items[self.size() - 1]
        self.items = self.items[0:-1]
        return item
