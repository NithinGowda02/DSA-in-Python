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
