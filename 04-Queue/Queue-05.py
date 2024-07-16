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


def initInput(inp):
    col_x, row_y, arr = inp.split(" ")
    col_x, row_y = int(col_x), int(row_y)
    out_range = "#" * col_x
    arr = out_range + "," + arr + "," + out_range
    arr = arr.split(",")
    if not len(arr) == row_y + 2:
        return None, None, None, None, None
    arr = ["#" + x + "#" for x in arr]
    for item in (arr):
        if not len(item) == col_x+2:
            return None, None, None, None, None
    # for line in arr:
    #     print(line)
    # print("")
    start = None
    end = None
    for y in range(1, len(arr) - 1):
        for x in range(1, len(arr[y]) - 1):
            if arr[y][x] == "F":
                start = (x, y)
            elif arr[y][x] == "O":
                end = (x, y)
    return start, end, col_x, row_y, arr
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
def findDirections(start_x_y, end_x_y, col_x, row_y, arr):
    q = Queue()
    visited = [[False] * (col_x + 2) for _ in range(row_y + 2)]
    parent_node = [[None] * (col_x + 2) for _ in range(row_y + 2)]
    q.enqueue(start_x_y)
    visited[start_x_y[1]][start_x_y[0]] = True

    # print("  0123456789")
    # for i, item in enumerate(arr):
    #     print(f"{i} {item}")
    # print("")
    while not q.is_empty():
        # print(f"---> {node}")
        if end_x_y in q.items:
            return True, parent_node
        print("Queue: ", end="")
        temp_print = []
        for i, coordinate in enumerate(q.items):
            newtpl  = (coordinate[0]-1,coordinate[1]-1)
            temp_print.append(newtpl)
        print(temp_print)
        node = q.dequeue()
        # print(f"Node : ({node[0]-1},{node[1]-1}) {arr[node[0]][node[1]][0]} ->", end="")
        for dx, dy in directions: ## for item in vector that u is node
            x, y = node
            ny, nx = y + dy, x + dx
            if 0 <= ny < row_y + 2 and 0 <= nx < col_x + 2 and not visited[ny][nx] and arr[ny][nx] in "_OF": # weight + u < vector
                # try:
                #     print(f"({nx-1},{ny-1} {arr[ny][nx]})", end="/")
                # except IndexError:
                #     print("Out", end="/")
                visited[ny][nx] = True
                parent_node[ny][nx] = node
                q.enqueue((nx, ny))
    return False, None
#     q = Queue()
#     visited = [[False] * (col_x + 2) for _ in range(row_y + 2)]
#     parent_node = [[None] * (col_x + 2) for _ in range(row_y + 2)]
#     q.enqueue(start)
#     visited[start[0]][start[1]] = True

#     while not q.is_empty():
#         node = q.dequeue()
#         print("Queue:", q.items)
#         if node == end:
#             return True, parent_node

#         for dy, dx in directions:
#             y, x = node
#             ny, nx = y + dy, x + dx
#             if 0 <= ny < row_y + 2 and 0 <= nx < col_x + 2 and not visited[ny][nx] and arr[ny][nx] in "FO_":
#                 visited[ny][nx] = True
#                 parent_node[ny][nx] = node
#                 q.enqueue((ny, nx))

#     return False, None


def main():
    inp = input("Enter width, height, and room: ")  # Example: 6 4 F__###,##_###,##__##,###__O
    start, end, col_x, row_y, arr = initInput(inp)
    #(x,y) (x,y) len(x) len(y) map

    if start is None :
        print("Invalid map input.")
        return
    found, parent_node = findDirections(start, end, col_x, row_y, arr)
    # found, parent_node = findDirections(start, end, col_x, row_y, arr)
    if found:
        print("Found the exit portal.")
        # Optional: Print the path
        # path = []
        # current_node = end
        # while current_node != start:
        #     x, y = current_node
        #     path.append((x - 1, y - 1))  # Convert grid coordinates to array indices (0-based)
        #     current_node = parent_node[y][x]
        # path.append(start)
        # path.reverse()
        # print("Path:", path)
    else:
        print("Cannot reach the exit portal.")
main()