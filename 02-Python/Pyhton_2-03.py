print(" *** Summation of each digit ***")
num = input("Enter a positive number : ")
sum = 0
for digit in str(num):  
    sum += int(digit)       
print("Summation of each digit = ",sum)