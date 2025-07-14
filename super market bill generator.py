# Supermarket Bill Generator using Dictionary

def generate_bill(cart):
    print("\n========= SUPERMARKET BILL =========")
    print("{:<15} {:<10} {:<10} {:<10}".format("Item", "Qty", "Price", "Total"))
    print("---------------------------------------------")

    grand_total = 0
    for item, details in cart.items():
        qty = details['qty']
        price = details['price']
        total = qty * price
        grand_total += total
        print("{:<15} {:<10} {:<10} {:<10}".format(item, qty, price, total))

    print("---------------------------------------------")
    print(f"Grand Total: ₹{grand_total:.2f}")
    print("Thanks for shopping! Come again 😊")
    print("=============================================")

# Main Program
cart = {}

while True:
    item = input("Enter item name (or 'done' to finish): ")
    if item.lower() == 'done':
        break

    if item in cart:
        print(f"{item} already in cart. Updating quantity and price.")
    try:
        qty = int(input(f"Enter quantity of {item}: "))
        price = float(input(f"Enter price per unit of {item}: "))
        cart[item] = {'qty': qty, 'price': price}
    except ValueError:
        print("Invalid input. Please enter numbers for quantity and price.")

# Print the bill
generate_bill(cart)# Supermarket Bill Generator using Dictionary

def generate_bill(cart):
    print("\n========= SUPERMARKET BILL =========")
    print("{:<15} {:<10} {:<10} {:<10}".format("Item", "Qty", "Price", "Total"))
    print("---------------------------------------------")

    grand_total = 0
    for item, details in cart.items():
        qty = details['qty']
        price = details['price']
        total = qty * price
        grand_total += total
        print("{:<15} {:<10} {:<10} {:<10}".format(item, qty, price, total))

    print("---------------------------------------------")
    print(f"Grand Total: ₹{grand_total:.2f}")
    print("Thanks for shopping! Come again 😊")
    print("=============================================")

# Main Program
cart = {}

while True:
    item = input("Enter item name (or 'done' to finish): ")
    if item.lower() == 'done':
        break

    if item in cart:
        print(f"{item} already in cart. Updating quantity and price.")
    try:
        qty = int(input(f"Enter quantity of {item}: "))
        price = float(input(f"Enter price per unit of {item}: "))
        cart[item] = {'qty': qty, 'price': price}
    except ValueError:
        print("Invalid input. Please enter numbers for quantity and price.")

# Print the bill
generate_bill(cart)
