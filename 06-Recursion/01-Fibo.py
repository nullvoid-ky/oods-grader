def fibo(num):
    if num <= 0:
        return "Input should be positive integer."
    elif num  <= 2:
        return 1
    return (fibo(num-1) + fibo(num-2))


inp = input("Enter Number : ")
num = int(inp)
print(f"fibo({num}) = {fibo(num)}")