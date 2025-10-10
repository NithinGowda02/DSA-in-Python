class car:
    def __init__(self, name, model, price, milage):
        self.name = name
        self.model = model
        self.price = price
        self.milage = milage

    def display(self):
        print(f"{self.name} comes in Model {self.model} with best price Segment ${self.price} with milage of {self.milage}") 

Toyata = car("Fortuner",2023,500000,8)
Maruthi_Suzuki = car("Omni",2005,18000,11)
Toyata.display()       
Maruthi_Suzuki.display() 
   