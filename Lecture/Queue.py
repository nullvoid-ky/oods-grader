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
    
    def __str__(self) -> str:
        return str(self.items)
    
    def is_empty(self):
        return self.size == 0
