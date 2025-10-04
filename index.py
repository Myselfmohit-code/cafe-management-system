menu = {
    "Coffee": 50,
    "Tea": 30,
    "Sandwich": 70,
    "Burger": 120,
    "Pasta": 150,
    "Pizza": 200,
    "Cake": 90,
    "Fries": 60,
    "Coke": 40,
    "Ice Cream": 80
}

sales = []

def show_menu():
    print("\n------ Cafe Menu ------")
    for item, price in menu.items():
        print(f"{item:10} : ₹{price}")
    print("-----------------------")

def take_order():
    order = {}
    while True:
        item = input("Enter item name (or 'done' to finish): ").title()
        if item == "Done":
            break
        elif item in menu:
            qty = int(input(f"Enter quantity of {item}: "))
            order[item] = order.get(item, 0) + qty
        else:
            print("Item not available. Please choose from the menu.")
    return order


def generate_bill(order):
    print("\n------ Bill ------")
    total = 0
    for item, qty in order.items():
        price = menu[item] * qty
        print(f"{item:10} x {qty} = ₹{price}")
        total += price
    print("-----------------")
    print(f"Total Bill : ₹{total}")
    print("-----------------")
    sales.append(total)


def show_sales():
    print("\n......... Sales History ........")
    if not sales:
        print("No sales yet.")
    else:
        for i, amount in enumerate(sales, 1):
            print(f"Order {i} : ₹{amount}")
        print(f"Total Earnings: ₹{sum(sales)}")
    print("---------------------------")


def cafe_system():
    while True:
        print("\n......... Cafe Management System .......")
        print("1. Show Menu")
        print("2. Take Order")
        print("3. Show Sales Report")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_menu()
        elif choice == "2":
            show_menu()
            order = take_order()
            if order:
                generate_bill(order)
            else:
                print("No items ordered.")
        elif choice == "3":
            show_sales()
        elif choice == "4":
            print("Exiting... Thank you! ☕")
            break
        else:
            print("Invalid choice! Please try again.")


cafe_system()
