class classRoom:
    def __init__(self, Student_Name, Roll_no):
        self.Student_Name = Student_Name
        self.Roll_no = Roll_no
        self.student_record = {}        # use instance record (avoid global name errors)
    
    def add_student(self):
        self.student_record[self.Student_Name] = self.Roll_no
        return self.student_record
    
    def remove_student(self, name=None):
        # allow removing by passed name (menu calls with a name)
        key = name if name is not None else self.Student_Name
        self.student_record.pop(key, None)
        return self.student_record
    
    def view_student(self):
        return self.student_record
    
class Student(classRoom):
    def __init__(self, Student_Name, Roll_no, marks, subject):
        super().__init__(Student_Name, Roll_no,)
        self.Student_Name = Student_Name
        self.Roll_no = Roll_no
        self.marks = marks
        self.subject = subject
        self.marks_record = {}

    def add_marks(self):
        self.marks_record[self.subject] = self.marks
        return self.marks_record

    def calculate_percentage(self):
        if not self.marks_record:
            return 0.0
        total = sum(self.marks_record.values())
        return total / len(self.marks_record)

    def result(self):
        percentage = self.calculate_percentage()
        if percentage >= 85:
            return "Distinction"
        elif percentage >= 60:
            return "First Class"
        elif percentage >= 50:
            return "Second Class"
        elif percentage >= 35:
            return "Third Class"
        else:
            return "Failed"

    def Calculate_Grade(self):
        for mark in self.marks_record.values():
            grade = ''
            if mark >= 90:
                grade = "A+"
                return grade
            
            elif mark >= 80:
                grade = "A"
                return grade
            
            elif mark >= 70:
                grade = "B+"
                return grade
            
            elif mark >= 60:
                grade = "B"
                return grade
            
            elif mark >= 50:
                grade = "C+"
                return grade
            
            elif mark >= 35:
                grade = "C"
                return grade
            
            else:
                grade = "FAIL"
                return grade

class Report_Card(Student):
    def __init__(self, Student_Name, Roll_no, marks, subject):
        super().__init__(Student_Name, Roll_no, marks, subject)

    def Generate_Report_Card(self):
        grade = self.Calculate_Grade()
        percentage = self.calculate_percentage()
        result = self.result()
        print("========================================================") 
        print(f"-----------------STUDENT REPORT CARD-------------------")
        print("========================================================")
        print("\tSUBJECT\t|\tMARKS\t|\tGRADE\t|\t")
        for subject, mark in self.marks_record.items():
            print(f"\t{subject}\t\t{mark}\t\t{grade}")
        print("========================================================")
        print(f"PERCENTAGE : {percentage}")
        print("========================================================")
        print(f"FINAL RESULT : {result}") 
        print("========================================================") 

def main():
    # minimal defaults so variables exist before they are assigned by user input
    student_name = ""
    section = ""
    roll_no = 0
    student_marks = []   # keep as iterable to avoid later division errors
    subject = ""

    student = Student(student_name, roll_no, student_marks, subject)
    report_card = Report_Card(student_name, roll_no, student_marks, subject)    
    while True:
        print("========================================================") 
        print(f"-----------------ADDING NEW STUDENT--------------------")
        print("========================================================") 
        print("1:Add new Student")
        print("2:Remove Student")
        print("3:View Student")
        print("4:Add Marks")
        print("5:Generate Report Card")
        print("6:Exit")
        choice = int(input("Choose your Operation >> "))
        if choice == 1:
            student_name = input("Enter the Student Name >> ")
            roll_no = int(input("Update the Roll Number >> "))
            # update the Student instance fields before adding
            student.Student_Name = student_name
            student.Roll_no = roll_no
            student.add_student()
            print("Student Added Succesfully...")
        elif choice == 2:
            del_name = input("Enter The Student name you Wanted to Delete >> ")   
            print("Student Deleted Succesfully...")
            student.remove_student(del_name)

        elif choice == 3:
                print("**********STUDENT DETAILS***********")
                print(student.view_student())

        elif choice == 4:
            name = input("Enter the Student Name >> ")
            if name in student.student_record:
                subject = input("Enter The Subject >> ")
                student_marks = int(input("Enter the Student Marks >>"))
                # update instance fields then add marks
                student.subject = subject
                student.marks = student_marks
                student.add_marks()
                print("Marks added.")
            else:
                     print("You are not Added the Student Details. Try Again after Adding")

        elif choice == 5:
            user_rollNo = int(input("Enter Your Roll Number >> "))
            # check if the entered roll number exists in stored roll numbers
            if user_rollNo in student.student_record.values():
                # copy current student's marks into report_card before printing
                report_card.Student_Name = student.Student_Name
                report_card.Roll_no = student.Roll_no
                report_card.marks_record = student.marks_record.copy()
                report_card.Generate_Report_Card()
            else:
                print("Invalid Roll Number! Try Again with Valid Roll Number.")   

        elif choice == 6:
            break         
            
        else:
            print("Invalid Choice!. Try Again") 
    

if __name__ == "__main__":
    main()











