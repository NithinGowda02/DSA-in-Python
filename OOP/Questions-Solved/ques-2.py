"""  Encapsulation:
 ○ Create a BankAccount class with private attributes for account _number and balance.
 ○ Add methods to check balance, deposit, and withdraw funds 
 ○ Try accessing the balance directly and observe the result
2. Abstraction:
Design a Phone class with methods to call_contact and take_picture . 
Abstract away any internal processing details and focus on creating a user-friendly interface
3. Inheritance:
Create a base class ehicle with a start method. Then create a subclass Bike with an additional ride() method. Demonstrate how the Bike can use both start and ride
4. Polymorphism:
D)
Implement a Shape class and derive Circle and Rectangle classes with a method calculate_area . Each class shoul calculate area differently based on its shape.
Create a loop to calculate areas for both Circle and Rectangle objects
        """


class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, add_amount):
        if self.__account_number == user_acc_num:
            self.__balance += add_amount
        else:
            print(f"Invalid Account Number!. Try again With Valid Account Number")    

    def withdraw_funds(self, withdrawed_ammount):
        if self.__account_number == user_acc_num:
            if withdrawal_amt <= self.__balance:
                self.__balance -= withdrawed_ammount
            else:
                print(f"Insufficient Funds. Your Balance >> {self.__balance}")    
        else:
            print(f"Invalid Account Number!. Try again With Valid Account Number")    

    def check_balance(self):
        if self.__account_number == user_acc_num:
            print(f"Your Account Balance >> {self.__balance}")   
        else:
            print(f"Invalid Account Number!. Try again With Valid Account Number")

Acc_holder = BankAccount(1234, 1000)             
while True:
    choice = int(input("Enter Your Choice [1.Deposit] [2.Withdrawal] [3.Check_Balance] [4.Exit] >> "))
    if choice == 1:
        user_acc_num = int(input("Enter your Account Number >> "))
        deposited_amt = int(input("Enter the Amount you wanted to deposit >> "))
        Acc_holder.deposit(deposited_amt)

    elif choice == 2:
        user_acc_num = int(input("Enter your Account Number >> "))
        withdrawal_amt = int(input("Enter the Amount you wanted to Withdraw >> "))
        Acc_holder.withdraw_funds(withdrawal_amt)

    elif choice == 3:
        user_acc_num = int(input("Enter your Account Number >> "))
        Acc_holder.check_balance()

    elif choice == 4:
        break

    else:
        print("Invalid Choice. Try Again with Valid Choice.")    

