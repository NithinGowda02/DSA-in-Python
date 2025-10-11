"""
4. Abstract Classes:
○ Define an abstract class Employee with an abstract method calculate_salary() . ◦ Create a subclass Manager that implements calculate_salary() based on working hours and rate per hour.
"""

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Manager(Employee):
    def calculate_salary(self):
        print("salary calculated") 

manager = Manager()
manager.calculate_salary()