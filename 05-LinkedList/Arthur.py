class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def print_list(self):
        current = self.head
        if not current:
            print("List is empty.")
            return
        # Print the list without the trailing ' -> None'
        while current:
            end_char = ' -> ' if current.next else ''
            print(current.data, end=end_char)
            current = current.next
        print()  # For a new line after the list

def merge_sort(head):
    if not head or not head.next:
        return head

    # Split the list into halves
    middle = get_middle(head)
    next_to_middle = middle.next

    middle.next = None
    next_to_middle.prev = None

    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    # Merge sorted halves
    return merge(left, right)

def get_middle(head):
    if not head:
        return head

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge(left, right):
    if not left:
        return right
    if not right:
        return left

    if left.data <= right.data:
        result = left
        result.next = merge(left.next, right)
        result.next.prev = result
        result.prev = None
    else:
        result = right
        result.next = merge(left, right.next)
        result.next.prev = result
        result.prev = None

    return result

# Create the doubly linked list with test case data
dll = DoublyLinkedList()
inp = input("Enter unsorted Linked List: ").split()
for value in inp:
    dll.append(value)

print("Before:", end=" ")
dll.print_list()

# Sort the list
dll.head = merge_sort(dll.head)

print("After :", end=" ")
dll.print_list()
