import random

class Bank:
    def create_account(self):
        holder_name = input("Enter the Account Holder Name >> ")
        account_type = input("Enter the Account type ([1.savings] [2.current]) >> ").lower()
        account_number = random.randint(1,11) * 123456789
        print(f"Your {account_type} Account Created Successfully \n Your Account Number : {account_number}")
        Bank_Record[holder_name] = account_number

class Account(Bank):
    def __init__(self):
        self._balance = 0
    def account_details(self):
        super().create_account()
    def Deposit(self, amount):
        self._balance += amount
        print(f"Deposit Successfull. Updated Balance >> {self._balance}")
    def Withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"Withdrawal Successfull. Updated Balance >> {self._balance}")
        else:
            print(f"Insufficient Funds..!")
    def Check_Balance(self):
        print(f"Your Current Balance >> {self._balance}")

class Savings_Account(Account):
    def __init__(self):
        self._balance = 0
        self.interest = 0.04
    def calculate_interest(self):
        interest = self._balance * self.interest
        print(f"Total Interest >> {interest}")

class Current_Account(Account):
    def __init__(self):
        self.OVERDRAFT_LIMIT = 1000
    def Withdraw(self, amount):
        if self._balance + self.OVERDRAFT_LIMIT >= amount:
            self._balance -= amount
            print(f"Withdrawal Successfull. Updated Balance >> {self._balance}")
        else:
            print(f"More Than OverDraft Limit. Try within the Limit")
new_Account = Bank()
account = Savings_Account()
cur_account = Current_Account()
Bank_Record = {}
print("WELCOME TO ** MY BANK OF INDIA **")
print("===================================")
while True:
    new_Account.create_account()
    while True:
        print("1.Savings")
        print("2.Current")
        select_type = int(input("Account Type (Savings / Current) >> "))
        while True:
            if select_type == 1:
                print("1.Deposit")
                print("2.Withdrawal")
                print("3.Check Balance")
                print("4.Check Interest")
                print("5.Exit")
                choice = int(input("Choose your operation >> "))
                if choice == 1:
                    amount = int(input("Enter the Amount You want Deposit >> "))
                    account.Deposit(amount)
                elif choice == 2:
                    amount = int(input("Enter the Amount You want Withdraw >> "))
                    account.Withdraw(amount)
                elif choice == 3:
                    account.Check_Balance()
                elif choice == 4:
                    account.calculate_interest()
                elif choice == 5:
                    break
                else:
                    print("Invalid Choice! Try Again")   
            elif select_type == 2:
                print("1.Deposit")
                print("2.Withdrawal")
                print("3.Check Balance")
                print("4.Exit")
                choice = int(input("Choose your operation >> "))
                if choice == 1:
                    cur_account.Deposit(amount=0)
                elif choice == 2:
                    cur_account.Withdraw(amount=0)
                elif choice == 3:
                    cur_account.Check_Balance()
                elif choice == 4:
                    break
                else:
                    print("Invalid Operation! Try Again")
            else:
                print("Invalid Operation! Try Again")        

                                





                                        

