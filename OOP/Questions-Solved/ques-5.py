"""4. Polymorphism:
Implement a Shape class and derive Circle and Rectangle classes with a method calculate_area . Each class shoul calculate area differently based on its shape.
Create a loop to calculate areas for both Circle and Rectangle objects
        """

class Shape:
    print("Calculated Area..")

class Circle(Shape):
    def __init__(self, rad):
        self.rad = rad
        
    def calculate_area(self):
        Area_of_Circle = (22/7)*self.rad*self.rad
        print(f"Area of Circle is >> {Area_of_Circle}")

class Rectangle(Shape):
     def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
     def calculate_area(self):
        Area_of_Rectangle = self.length * self.breadth
        print(f"Area of Rectangle is >> {Area_of_Rectangle}")

rectangle = Rectangle(4,7)
circle = Circle(2)
area = [rectangle, circle]
for i in area:
    i.calculate_area()