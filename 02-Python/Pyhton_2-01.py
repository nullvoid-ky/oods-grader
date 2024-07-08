

class translator:
    def __init__(self):
        self.dictionary : dict = {
            "I":1,
            "IV":4,
            "V":5,
            "IX":9,
            "X":10,
            "XL":40,
            "L":50,
            "XC":90,
            "C":100,
            "CD":400,
            "D":500,
            "CM":900,
            "M":1000,
        }
    def deciToRoman(self, num):
        text = ""
        while num >= 1000:
            num -= 1000
            text += "M"
        while num > 0:
            oldValue :int = 0
            oldWord :str = ""
            for word, value in self.dictionary.items():
                if num < value:
                    num-=oldValue
                    text += oldWord
                    break
                oldValue = value
                oldWord = word
        return text

    def romanToDeci(self, s):
        num = 0
        while len(s) > 0:
            for word, value in self.dictionary.items():
                if s == "":
                    break
                elif s[-2:] == word:
                    num+=value
                    s = s[:-2]
                elif s[-1:] == word :
                    num+=value
                    s = s[:-1]
        return num

num = int(input("Enter number to translate : "))
Translator = translator()
print(Translator.deciToRoman(num))
print(Translator.romanToDeci(Translator.deciToRoman(num)))