def pow (num, power, answer):
    if power > 0:
        answer *= num
        return pow(num, power-1, answer)
    return answer
inp = input("Enter Input a b : ")
a, b = inp.split()
a, b = int(a), int(b)
print(pow(a, b, 1))