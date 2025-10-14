import random

class Bank:
    def create_account(self, holder_name, account_type, account_number):
        self.holder_name = holder_name
        self.account_type = account_type
        self.account_number = account_number
        print(f"Your {self.account_type} Account Created Successfully \n Your Account Number : {self.account_number}")
        Bank_Record[holder_name] = self.account_number

class Account(Bank):
    def __init__(self):
        self._balance = 0
        
    def Deposit(self):
        Acc_num_input = int(input("Enter Your Account Number >> "))    
        if Bank_Record[holder_name] == Acc_num_input:
            amount = int(input("Enter the Amount You want Deposit >> "))
            self._balance += amount
            print(f"Deposit Successfull. Updated Balance >> {self._balance}")
        else:
            print("Invalid Account Number..! Try Again with Valid Account Number")     
    def Withdraw(self):
        Acc_num_input = int(input("Enter Your Account Number >> "))    
        if Bank_Record[holder_name] == Acc_num_input: 
            amount = int(input("Enter the Amount You want Withdraw >> "))   
            if self._balance >= amount:
                self._balance -= amount
                print(f"Withdrawal Successfull. Updated Balance >> {self._balance}")
            else:
                print(f"Insufficient Funds..!")
        else:
            print("Invalid Account Number..! Try Again with Valid Account Number")         
    def Check_Balance(self):
        Acc_num_input = int(input("Enter Your Account Number >> "))    
        if Bank_Record[holder_name] == Acc_num_input:
            print(f"Your Current Balance >> {self._balance}")
        else:
            print("Invalid Account Number..! Try Again with Valid Account Number")    

class Savings_Account(Account):
    def __init__(self):
        self._balance = 0
        self.interest = 0.04
    def calculate_interest(self):
        interest = self._balance * self.interest
        print(f"Total Interest >> {interest}")

class Current_Account(Account):
    def __init__(self):
        self._balance = 0
        self.OVERDRAFT_LIMIT = 1000
    def Withdraw(self):
        Acc_num_input = int(input("Enter Your Account Number >> "))    
        if Bank_Record[holder_name] == Acc_num_input: 
            amount = int(input("Enter the Amount You want Withdraw >> "))   
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
    print("Creating Your Account".upper())
    print("===================================")
    holder_name = input("Enter the Account Holder Name >> ")
    account_type = input("Enter the Account type ([1.savings] [2.current]) >> ").lower()
    account_number = random.randint(1,11) * 123456789
    new_Account.create_account(holder_name, account_type, account_number)
    while True:
        print("========================================================")
        print("FOR FURTHER BANKING OPERATION SELECT YOUR ACCOUNT TYPE")
        print("========================================================")
        print("1.Savings")
        print("2.Current")
        print("3.Exit")
        print("========================================================")
        select_type = int(input("Account Type (Savings / Current) >> "))
        while True:
            if select_type == 1:
                print("===============================")
                print("AVAILAIBLE BANKING OPERATION")
                print("===============================")
                print("1.Deposit")
                print("2.Withdrawal")
                print("3.Check Balance")
                print("4.Check Interest")
                print("5.Exit")
                print("===============================")
                choice = int(input("Choose your operation >> "))
                if choice == 1:
                    account.Deposit()
                elif choice == 2:
                    account.Withdraw()
                elif choice == 3:
                    account.Check_Balance()
                elif choice == 4:
                    account.calculate_interest()
                elif choice == 5:
                    print("=======================================================")
                    break
                else:
                    print("Invalid Choice! Try Again")   
            elif select_type == 2:
                print("===============================")
                print("AVAILAIBLE BANKING OPERATION")
                print("===============================")
                print("1.Deposit")
                print("2.Withdrawal")
                print("3.Check Balance")
                print("4.Exit")
                print("===============================")
                choice = int(input("Choose your operation >> "))
                if choice == 1:
                    cur_account.Deposit()
                elif choice == 2:
                    cur_account.Withdraw()
                elif choice == 3:
                    cur_account.Check_Balance()
                elif choice == 4:
                    print("=======================================================")
                    break
                else:
                    print("Invalid Operation! Try Again")
            elif select_type == 3:
                print("=======================================================")
                break        
            else:
                print("Invalid Operation! Try Again")
             
        break   


                                





                                        

