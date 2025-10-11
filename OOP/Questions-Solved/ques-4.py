"""3. Inheritance:
Create a base class ehicle with a start method. Then create a subclass Bike with an additional ride() method. Demonstrate how the Bike can use both start and ride"""

class Vechicle:
    def __init__(self, name):
        self.name = name
    def start(self):
        print(f"{self.name} is Started..")

class Bike(Vechicle):
    def ride(self):
        print(f"{self.name} is riding")  

b = Bike("Xpulse")
b.start()
b.ride()              
