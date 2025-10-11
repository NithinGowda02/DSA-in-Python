"""2. Abstraction:
Design a Phone class with methods to call_contact and take_picture . 
Abstract away any internal processing details and focus on creating a user-friendly interface"""

class phone:
    def Take_Picture(self):
        print("Picture Taken")

    def call_contact(self):
        print("Called to Contact")  

nokia = phone()
nokia.call_contact()
nokia.Take_Picture()          