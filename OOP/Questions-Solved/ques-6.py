"""
1. Getters and Setters:
○ Create a class BankAccount with a private attribute balance
○ Write a getter method to retrieve the balance and a setter method to update it, en suring the balance never goes below zero.
"""

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, updated_balance):
        self.__balance = updated_balance
        return self.__balance
    
balance = BankAccount(1000)
print(f"Balance >> {balance.get_balance()}")
print(f"Balance >> {balance.set_balance(1500)}")    