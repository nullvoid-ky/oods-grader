


class Spherical:

    def __init__(self,r):
        self.radius = r
        self.pi = 3.1415926535897932384626433832795028841
        ### Enter Your Code Here ###

    def changeR(self,Radius):
        self.radius = Radius
        ### Enter Your Code Here ###

    def findVolume(self):
        return (4/3*self.pi*(self.radius**3))
        ### Enter Your Code Here ###

    def findArea(self):
        return (4*self.pi*(self.radius**2))
        ### Enter Your Code Here ###

    def __str__(self):
        return f"Radius ={self.radius} Volumn = {self.findVolume()} Area = {self.findArea()} "
        ### Enter Your Code Here ###

(r1, r2) = input("Enter R : ").split(" ")
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)


