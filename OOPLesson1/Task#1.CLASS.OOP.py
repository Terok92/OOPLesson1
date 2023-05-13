class Rectangle:
    def __init__(self, length, width):
        self.width = width
        self.length = length

    def findarea(self):
        return self.width * self.length

    def findperimeter(self):
        return 2 * (self.width + self.length)


print("show me perimeter and and area of my rectangle:\t")
length = int(input("Enter a length:\n"))
width = int(input("Enter a width:\n"))
Rectangle1 = Rectangle(length, width)
print("Area is ", Rectangle1.findarea())
print("Perimeter is ", Rectangle1.findperimeter())
