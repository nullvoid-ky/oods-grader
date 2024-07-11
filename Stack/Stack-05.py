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

print("******** Parking Lot ********")
size,carlist,operation,car = input("Enter max of car,car in soi,operation : ").split()
size,car = int(size),int(car)
if "," in carlist:
    carlist = list(map(int,list(carlist.split(","))))
else:
    carlist = [int(carlist)] if int(carlist) > 0 else None


a = Stack(carlist)
if operation == "arrive":
    if a.size < size:
        if a.has(car):
            print(f"car {car} already in soi")
        else :
            a.push(car)
            print(f"car {car} arrive! : Add Car {car}")
    else:
        print(f"car {car} cannot arrive : Soi Full")
elif operation == "depart":
    if a.has(car):
        a.remove(car)
        print(f"car {car} depart ! : Car {car} was remove")
    else:
        if a.is_empty():
            print(f"car {car} cannot depart : Soi Empty")
        else:
            print(f"car {car} cannot depart : Dont Have Car {car}")
print(f"{a}")
exit()
# elif operation == "depart":
    # """"""