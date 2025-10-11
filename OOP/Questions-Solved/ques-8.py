"""
3. Method Overriding:
O Create a parent class Shape with a method draw() that prints "Drawing shape" ○ Create a child class Circle that overrides draw() to print "Drawing circle"
"""

class Shape:
    def draw(self):
        print("drawing Shape")

class Circle(Shape):
    def draw(self):
        super().draw()
        print("drawing Circle")

c = Circle()
c.draw()