
menu = {
    'pizza': 60,
    'Pasta': 40,
    'Burger': 60,
    'salad': 70,
    'coffee': 80,
    'Momozz':90,
    'spring_roll':80,

}

print("Welcome to BIHARI Restaurant 🎊😍")
print("pizza: 60 Rs\nPasta: 40 Rs\nBurger: 60 Rs\nsalad: 70 Rs\ncoffee: 80 Rs")

order_total = 0


item = input("Enter the item you want to order: ")
if item in menu:
        order_total += menu[item]
        print(f"Your item {item} has been added to your order")
else:
        print(f"Ordered item {item} is not availabe yet in  menu")

another_order = input("Do you want to add another item? (yes/no): ")
if another_order == "yes":
        item2 = input("enter the name of second items:")
        if item2 in menu:
            order_total += menu[item2]
            print(f"item{item2} has been added to order")
        else:
            print(f"item {item2} is not available ")

print(f"The total amount of item to pay is {order_total} Rs")