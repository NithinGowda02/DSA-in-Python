stack = []

def push():
    if len(stack) >= 3:
        print("Stack is Full")
    else:    
        Add_item = int(input("enter the element you want push to Stack.. >> "))
        stack.append(Add_item)
        print(stack)

def pop():
    if len(stack) == 0:
        print("Stack is Empty") 
    else:
        stack.pop()
        print(stack)

def top():
    if len(stack) == 0:
        print("Stack is Empty")
    else:
        top=stack[-1]
        print("Top element >> ",top)

while True:
    choice = int(input("Enter your choice ([1:Push] [2:Pop] [3:Top Element] [4:Exit])>> "))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        top()
    elif choice == 4:
        break
    else:
        print("Invalid choice...!")                        
    

    