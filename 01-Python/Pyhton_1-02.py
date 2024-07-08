print("*** multiplication or sum ***")
str = input("Enter num1 num2 : ")
num1 = int(str.split(" ")[0])
num2 = int(str.split(" ")[1])
if num1*num2<=1000:
    print("The result is",num1*num2)
else:
    print("The result is",num1+num2)

