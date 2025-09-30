def grocery_shop():
    # Step 1: Shop items with price
    shop_items = {
        1: ("Rice", 50),
        2: ("Wheat", 40),
        3: ("Sugar", 35),
        4: ("Milk", 25),
        5: ("Oil", 120)
    }

    # Step 2: Print shop items
    print("----- Welcome to My Grocery Shop -----")
    print("Available Items:")
    for key, value in shop_items.items():
        print(f"{key}. {value[0]} - Rs.{value[1]}")

    # Step 3 & 4: Take user input and store in cart
    cart = {}

    while True:
        choice = int(input("\nEnter item number to buy (0 to proceed to payment): "))
        if choice == 0:
            break
        elif choice in shop_items:
            qty = int(input(f"Enter quantity for {shop_items[choice][0]}: "))
            
            # Add to cart dictionary
            if shop_items[choice][0] in cart:
                cart[shop_items[choice][0]] += qty
            else:
                cart[shop_items[choice][0]] = qty
        else:
            print("Invalid choice, try again.")

        # Step 5: Option to continue or checkout
        more = input("Do you want to add more items? (yes/no): ").lower()
        if more != "yes":
            break

    # Step 6: Generate Bill
    print("\n----- Your Bill -----")
    total = 0
    for item, qty in cart.items():
        # Find price from shop_items
        price = [price for name, price in shop_items.values() if name == item][0]
        cost = qty * price
        total += cost
        print(f"{item} x {qty} = Rs.{cost}")

    print("----------------------------")
    print(f"Total Amount: Rs.{total}")
    print("Thank you for shopping with us! 🙏")


# Run the shop
grocery_shop()