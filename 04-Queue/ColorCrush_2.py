
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

def explosiveCheck(bomb):
    s = Stack()
    output = []
    txt = bomb
    size_s = Stack()
    count_combo = 0
    i = -1
    for item in txt:
        i+=1
        if s.is_empty():
            s.push(item)
            tpl = (1,item)
            size_s.push(tpl)
        elif s.peek() == item:
            old , temp  = size_s.peek()
            old = int(old)
            size_s.pop()
            tpl = (old + 1, item)
            size_s.push(tpl)
            s.push(item)
        else:
            tpl = (1, item)
            size_s.push(tpl)
            s.push(item)
        if (size_s.peek()[0] >= 3):
            size_s.pop()
            explosion = s.pop()
            output.append(explosion)
            for _ in range(2):
                s.pop()
            count_combo += 1
    return (output, s.items, count_combo)

def explosiveBoom(bomb, mirror):
    s = Stack()
    txt = bomb
    q = Queue(mirror)
    size_s = Stack()
    count_combo = 0
    fail = 0
    i = -1
    for item in txt:
        i+=1
        if s.is_empty():
            s.push(item)
            tpl = (1,item)
            size_s.push(tpl)
        elif s.peek() == item:
            old , temp  = size_s.peek()
            old = int(old)
            size_s.pop()
            tpl = (old + 1, item)
            size_s.push(tpl)
            s.push(item)
        else:
            tpl = (1, item)
            size_s.push(tpl)
            s.push(item)
        if (size_s.peek()[0] >= 3 and not q.is_empty()):
            explosion = s.pop()
            mirror = q.pop()
            s.push(mirror)
            s.push(explosion)
            if not mirror == explosion:
                size_s.pop()
                tpl1 = (2, explosion)
                tpl2 = (1, mirror)
                tpl3 = (1, explosion)
                size_s.push(tpl1)
                size_s.push(tpl2)
                size_s.push(tpl3)
            else:
                size_s.pop()
                tpl = (4, explosion)
                size_s.push(tpl)
                fail+=1
        if (size_s.peek()[0] == 3):
            size_s.pop()
            for _ in range(3):
                s.pop()
            count_combo += 1
        elif (size_s.peek()[0] > 3):
            sz, temp = size_s.peek()
            size_s.pop()
            exp = s.pop()
            tpl = (sz-3, exp)
            size_s.push(tpl)
            for _ in range(2):
                s.pop()
    return (s.items, count_combo, fail)

inp = input("Enter Input (Normal, Mirror) : ") #AAABBBCDDDEE BBBTENETAAA
normal, mirror = inp.split(" ")
normal, mirror = list(normal),list(mirror)
mirror.reverse()
bomblist, bombleft, bombcombo= explosiveCheck(mirror)
bombleft.reverse()
bombleft = ''.join(bombleft)
# print(bomblist)
# print(bombleft)
# print(bombcombo)
postplant, combo, fail= explosiveBoom(normal, bomblist)
postplant.reverse()
postplant = ''.join(postplant)
# print(postplant)
# print(combo)
# print(fail)
    

print("NORMAL :")
print(len(postplant))
if len(postplant):
    print(postplant)
else:
    print("Empty")
print(f"{combo} Explosive(s) ! ! ! (NORMAL)")
if fail:
    print(f"Failed Interrupted {fail} Bomb(s)")
print("------------MIRROR------------")
print(": RORRIM")
print(len(bombleft))
if len(bombleft):
    print(bombleft)
else:
    print("ytpmE")
print(f"(RORRIM) ! ! ! (s)evisolpxE {bombcombo}")
