class Shapes:
    def __init__(self, shape):
        self.shape = shape
    def area(self):
        pass
    def perimeter(self):
        pass
class Rectangle(Shapes):
    def __init__(self, length, breadth):
        super().__init__("Rectangle")
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)
class Square(Shapes):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side
class Triangle(Shapes):
    def __init__(self, base, height, s1, s2, s3):
        super().__init__("Triangle")
        self.base = base
        self.height = height
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.s1 + self.s2 + self.s3

square = Square(int(input("Enter the side of square: ")))
print("Area of square:", square.area())
print("Perimeter of square:", square.perimeter())

rectangle = Rectangle(int(input("Enter the length of rectangle: ")), int(input("Enter the breadth of rectangle: ")))
print("Area of rectangle:", rectangle.area())
print("Perimeter of rectangle:", rectangle.perimeter())

triangle = Triangle(int(input("Enter the base of triangle: ")), int(input("Enter the height of triangle: ")), int(input("Enter the first side of triangle: ")), int(input("Enter the second side of triangle: ")), int(input("Enter the third side of triangle: ")))
print("Area of triangle:", triangle.area())
print("Perimeter of triangle:", triangle.perimeter())