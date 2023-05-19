class Rectangle:
    def __init__(self):
        self.width = width
        self.length = length

    def findarea(self):
        return self.width * self.length

    def findperimeter(self):
        return 2 * (self.width + self.length)


print("perimeter and  area of my rectangle:\n")
length = int(input("Enter a length:\n"))
width = int(input("Enter a width:\n"))
Rectangle1 = Rectangle()
print("Area is ", Rectangle1.findarea())
print("Perimeter is ", Rectangle1.findperimeter())
