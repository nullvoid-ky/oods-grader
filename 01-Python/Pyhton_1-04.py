print("*** Fun with Drawing ***")
num = int(input("Enter input : "))
for i in range(1, num+1):
    print("."*(num-i), end="")
    print("*", end="")
    print("+"*(i-1), end="")
    print("+"*(i-2), end="")
    if i > 1:
        print("*", end="")
    print("."*(num-i), end="")
    print("."*(num-i-1), end="")
    if i < num:
        print("*", end="")
    print("+"*(i-1), end="")
    print("+"*(i-2), end="")
    if i > 1:
        print("*", end="")
    print("."*(num-i), end="")
    print("")

size = (num*2)-2
for i in range(1, size+1):
    print("."*(i), end="")
    print("*", end="")
    print("+"*(size-i), end="")

    print("+"*(size-i-1), end="")
    if i <size:
        print("*", end="")
    print("."*(i), end="")
    print("")
