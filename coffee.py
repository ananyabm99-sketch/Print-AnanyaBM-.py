'''Coffee machine'''

menu = [{
    "expresso": 
    {
        "Milk":100,
        "Water":50,
        "sugar":30,
        "Bru":20
        },
    "cost":5
},
{
    "latte": 
    {
        "Milk":150,
        "Water":50,
        "sugar":60,
        "Bru":20
        },
    "cost":10
},
{
    "capuccino": 
    {
        "Milk":150,
        "Water":50,
        "sugar":60,
        "Bru":40
        },
    "cost":15
}]
resource = {
    "Milk":1000,
    "Water":1000,
    "Sugar":500,
    "Bru":500
}
profit = 0
def money_analyser(money):
    global profit
    print("please insert coins:")
    coin_type = int(input("Enter the type of coin:(5/10):"))
    coin_number = int(input("Enter the number of coins:"))
    total_number = coin_type * coin_number
    if total_number >= item["cost"]:
        change = total_number - item["cost"]
        print(f"Here is your change : {change}")
        profit += item["cost"]
    else:
        print("Sorry that's not enough money. Money refunded.")

def resource_analyser():
    global resource
    for item in menu:
        for choice in item:
            for i in item[choice]:
                resource[i] -= item[choice][i]
                if resource[i] < item[choice][i]:
                    print("Sorrey there is not enough resources!!")
                return False
            return True
            
is_enough = True
while is_enough:
    print("___________________Welcome to coffee Machine_______________\n")
    print("Expresso:5\nLatte:10\nCappucino:15")
    choice = input("What do you like to drink?(Expresso/Latte/Capuccino):").lower()
    for item in menu:
        if choice in item :
            print(item[choice])
            print("Resource")
            print(resource)
            money_analyser(item["cost"])
            resource_analyser()
            print("Here is your coffee ☕️. Enjoy!")
            input("Do you want to continue drinking coffee?(yes/no):").lower()
            if choice == "no":
                is_enough = False
                print("Thank you ! ,Have a nice day")
                break
            else:
                is_enough = True