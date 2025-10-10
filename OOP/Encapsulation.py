class Bank:
    def __init__(self, __acc_num, __Balance):
        self.__acc_num = __acc_num
        self.__Balance = __Balance

    def Check_Balance(self):
        print(f"Acc no : {self.__acc_num} has Current Balance >> {self.__Balance}")  

check_bal = Bank(12345, 413)
check_bal.Check_Balance()



