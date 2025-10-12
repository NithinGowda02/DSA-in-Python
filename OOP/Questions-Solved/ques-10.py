
class calculator:
    def addition(self, num1, num2):
        print(f"Result : {num1 + num2}")
    
    def substraction(self, num1, num2):
        print(f"Result : {num1 - num2}")
    
    def multiplication(self, num1, num2):
        print(f"Result : {num1 * num2}")
    
    def division(self, num1, num2):
        print(f"Result : {num1 / num2}")
    
sim_calculator = calculator()
while True:
    print("Simple Calculator")
    print("===================")
    print("""1.Addition
2.Substraction
3.Multiplication
4.Division
5.Exit""")
    choice = int(input("Enter your choice (1-5) >> "))  
    if choice == 1:
        num1 = int(input("Enter the first number >> "))   
        num2 = int(input("Enter the second number >> "))
        sim_calculator.addition(num1, num2)
    elif choice == 2:
        num1 = int(input("Enter the first number >> "))   
        num2 = int(input("Enter the second number >> "))
        sim_calculator.substraction(num1, num2)
    elif choice == 3:
        num1 = int(input("Enter the first number >> "))   
        num2 = int(input("Enter the second number >> "))
        sim_calculator.multiplication(num1, num2) 
    elif choice == 4:
        num1 = int(input("Enter the first number >> "))   
        num2 = int(input("Enter the second number >> "))
        sim_calculator.division(num1, num2) 
    elif choice == 5:
        break
    else:
        print("Invalid Choice!. Try Again with valid choice...")
print("Exiting the Calculator. Goodbye!")                   
