"""
2. Method Overloading:
○ Write a class Calculator with a method multiply() . Allow it to take either two or three arguments to multiply two or three numbers."""

class Calculator:
    def multifly(self, num1, num2, num3=1, num4=1):
        print(f"Multiplication of 2 Number >> {num1 * num2}")
        print(f"Multiplication of 3 Number >> {num1 * num2 * num3}")
        print(f"Multiplication of 4 Number >> {num1 * num2 * num3 * num4}")
calci = Calculator()

calci.multifly(23, 24, 88)
       
