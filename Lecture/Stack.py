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
        return item == self.items
    def index(self, item):
        return self.items.index(item) if item in self.items else -1
    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
            self.size -= 1
    def sort(self):
        self.items.sort()
    def remove_duplicates(self):
        self.items = list(set(self.items))
    def merge(self, other):
        return Stack(self.items + other.items)
    def emplace(self, items):
        self.items.extend(items)
        self.size += len(items)

    

# Example usage:
stack = Stack([1, 2, 3, 4, 5])
print(stack)  # Output: [1, 2, 3, 4, 5]

stack.push(6)
print(stack)  # Output: [1, 2, 3, 4, 5, 6]


print(stack.pop())  # Output: 6
print(stack)  # Output: [1, 2, 3, 4, 5]

print(stack.peek())  # Output: 5

print(stack.is_empty())  # Output: False

stack.clear()
print(stack)  # Output: []

stack.push(1)


stack.reverse()
print(stack)  # Output: [1]

stack.push(2)
stack.push(3)
stack.reverse()
print(stack)  # Output: [3, 2, 1]

print(stack.has(2))  # Output: True
print(stack.has(7))  # Output: False

print(stack.index(2))  # Output: 1
print(stack.index(7))  # Output: -1

stack.remove(2)
print(stack)  # Output: [3, 1]

stack.sort()
print(stack)  # Output: [1, 3]

stack.remove_duplicates()
print(stack)  # Output: [1, 3]

stack2 = Stack([4, 5, 6])
merged_stack = stack.merge(stack2)
print(merged_stack)  # Output: [1, 3, 4, 5, 6]

stack.emplace([7, 8, 9])
print(stack)  # Output: [1, 3, 4, 5, 6, 7, 8, 9]

stack.remove_duplicates()
print(stack)  # Output: [1, 3, 4, 5, 6, 7, 8, 9]

stack.clear()
print(stack)  # Output: []

stack.emplace([1, 2, 3])
stack.emplace([4, 5, 6])
print(stack)  # Output: [1, 2, 3, 4, 5, 6]

print(stack.size) 
print(stack.items) 
print(stack.size)