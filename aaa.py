def menu():
    m = {
        1: ("Chicken full meals", 200),
        2: ("Maten full meals", 250),
        3: ("Kal soup", 300),
        4: ("Khima", 100),
        5: ("Biryani", 120),
        6: ("Bowbow Biryani", 10),
        7: ("Kurma", 60),
        8: ("Kabab", 50),
        9: ("Bootigojju", 250),
        10: ("Chilli chicken", 60),
        11: ("Tandoori chicken", 300),
        12: ("Pepper fry", 100)
    }
    

    print("---- MENU ----")
    for key, value in m.items():
        print(f"{key}. {value[0]} : ₹{value[1]}")
    return m
menu_dict = menu()  
def x():
    print("1.Order")
    print("2.payment")
    print("3.Exit")
 
print(" "*42)
total  = 0
while  True :
    x()
    Choice = int(input("Enter your choice: "))
    if Choice == 1:
        dish_no = int(input("Enter the num of dish: "))
        if dish_no  in menu_dict:
            qty = int(input("Enter the quantity: "))
            cost = menu_dict [dish_no][1]* qty
            total += cost
        else:
            print("Invalid dish_no")    
    elif Choice == 2:
        print(f"Your bill is ₹{total}\n")
        print("Thank you for ordering!")
        break
    elif Choice == 3:
        print("GoodBye")
        break
    else:
        print("Invalid choice")    
        
        
        
        
                
            
        