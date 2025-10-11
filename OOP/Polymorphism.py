class Shape:
    def __init__(self, rad, pi):
        self.rad = rad
        self.pi = pi

class Circle(Shape):
    def calculate_area(self):
        Area_of_Circle = self.pi*self.rad*self.rad
        print(f"Area of Circle is >> {Area_of_Circle}")

class Rectangle(Shape):
     def calculate_area(self):
        Area_of_Rectangle = 2*self.pi*self.rad
        print(f"Area of Rectangle is >> {Area_of_Rectangle}")

rectangle = Rectangle(4,3.142)

rectangle.calculate_area()
circle = Circle(2, 3.142)
circle.calculate_area()