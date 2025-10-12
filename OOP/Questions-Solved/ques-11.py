def menu():
    print("1.Add item")
    print("2.Remove item")
    print("3.Total Amount")
    print("4.Exit")

cart =dict()
def add_item():
    print("1.Milk : 40")
    print("2.Sugar : 50")
    print("3.Salt : 25")
    print("4.Chilli Powder : 75")
    print("5.Curd : 40")
    print("6.Onion : 30")
    print("7.Tomato : 25")
    print("8.Biscuit : 20")
    print("9.Exit")
    while True:
        choose = int(input("Choose items to that you want to put in cart >> "))  
        if choose == 1:
            cart["milk"] = 40
        elif choose == 2:
            cart["sugar"] = 50
        elif choose == 3:
            cart["salt"] = 25
        elif choose == 4:
            cart["chilli powder"] = 75
        elif choose == 5:
            cart["curd"] = 40
        elif choose == 6:
            cart["0nion"] = 30
        elif choose == 7:
            cart["tomato"] = 25
        elif choose == 8:
            cart["biscuit"] = 20
        elif choose == 9:
            break 
        else:
            print("Invalid item!. Check the List")
    print(f"CART >> {cart}")        

def remove_item():
    print(f"CART >> {cart}")
    del_item = input("Enter the item you want to remove >> ").lower()
    cart.pop(del_item)
    print(f"CART >> {cart}")

def total_amount():
    total_cost = 0
    item_count = 1
    print("List Of Items")
    print("***************")
    for item, price in cart.items():
        print(f"{item_count}. {item} >> {price}")
        total_cost +=price
        item_count += 1
    print(f"Total Cost of Items >> {total_cost}")  

while True:
    menu()
    choice = int(input("Choose Your Operation >> "))
    if choice == 1:
        add_item()
    elif choice == 2:
        remove_item()
    elif choice == 3:
        total_amount()
    elif choice == 4:
        break
    else:
        print("Invalid Choice!, Try Again...")                     
