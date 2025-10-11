# Create a Class Employee with method 'display_info' with attributes name, designation and salary with default value 30000.

class Employee:
    def __init__(self, name, designation, salary = 30000):
        self.name = name
        self.designation = designation
        self.salary = salary
    def display_info(self):
        print(f"{self.name} work has a {self.designation} for salary of {self.salary}")

emp1 = Employee("Nithin K P", "Software Engineer", 100000)
emp2 = Employee("Madan", "Font-end Developer")        
emp1.display_info() 
emp2.display_info()    