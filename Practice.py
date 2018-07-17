class Fruit:
    def __init__(self, color, shape, taste):
        self.color = color
        self.shape = shape
        self.taste = taste

class Sweet(Fruit):
    def sweet(self):
        print("Yummy!")

class Sour(Fruit):
    def sour(self):
        print("Pucker!")

Grape = Sweet("Purple", "Sphere", "Sweet")
Lemon = Sour("Yellow", "Oblate Spheroid", "Sour")

print(Grape.shape)
print(Lemon.shape)
Lemon.sour()
Grape.sweet()