class Queue:
    def __init__(self, lst=None):
        self.items = lst if lst is not None else []
        self.size = len(self.items)

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.items.pop(0)

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

print(" ***Cafe***")
inp = input("Log : ")  
lst = inp.split("/")   
lst = [tuple(map(int, l.split(","))) for l in lst]  
q = Queue(lst)
b1 = b2 = 0
most = 0
wait_index = 0
i = 0
output = []
while not q.is_empty():
  i += 1
  current = q.dequeue()
  if b1 >= b2 and current[0] <= b1:
    b1, b2 = b2, b1
  if current[0] > b1:
    b1 = current[0]
  if most < b1 - current[0]:
    most = b1 - current[0]
    wait_index = i
  b1 += current[1]
  output.append([b1, i])
output.sort()
for itr in output:
  print(f'Time {itr[0]} customer {itr[1]} get coffee')
if wait_index == 0 and most == 0:
  print('No waiting')
else:
  print(f'The customer who waited the longest is : {wait_index}')
  print(f'The customer waited for {most} minutes')