class Stack:
    def __init__(self, lst = None):
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
    def __str__(self):
        return str(self.items)
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

s = Stack()
inp = input("Enter Input : ") 
txt = inp.split()
size_s = Stack()
count_combo = 0
i = -1
for item in txt:
    i+=1
    if s.is_empty():
        # print(f"{i} init {item}")
        s.push(item)
        tpl = (1,item)
        size_s.push(tpl)
    elif s.peek() == item:
        # print(f"{i} continue {item}")
        old , temp  = size_s.peek()
        old = int(old)
        size_s.pop()
        tpl = (old + 1, item)
        size_s.push(tpl)
        s.push(item)
    else:
        # print(f"{i} add other {item}")
        tpl = (1, item)
        size_s.push(tpl)
        s.push(item)

    if (size_s.peek()[0] >= 3):
        size_s.pop()
        for _ in range(3):
            s.pop()
        count_combo += 1
post_size = s.size
print(post_size)
while(not s.is_empty()):
    print(s.peek(), end="")
    s.pop()
if post_size == 0:
    print("Empty")
else:
    print("")
if count_combo > 1:
    print(f"Combo : {count_combo} ! ! !")
    