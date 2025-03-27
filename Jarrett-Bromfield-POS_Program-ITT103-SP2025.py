'''First we create a dictionary to store the products name, price and quantity available in stock.'''
products = {
    "Milk": {"price": 750, "quantity": 12},
    "Rice": {"price": 950, "quantity": 13},
    "Flour": {"price": 935, "quantity": 16},
    "Sugar": {"price": 890, "quantity": 10},
    "Water": {"price": 125, "quantity": 16},
    "Bigga Soda": {"price": 200, "quantity": 10},
    "Insect Spray": {"price": 545, "quantity": 13},
    "Bleach": {"price":465, "quantity": 10},
    "Shopping Bag":{"price":160, "quantity": 120}
}
# next we create the empty dictionary, this represents the customers shopping cart.
cust_cart = {}
'''The checkout_cart function will check if the item is in stock, in whatever quantity is required, 
if it is available, it will be added to the customers cart, if not an error message will be displayed and the user will be prompted to re-enter a different quantity'''

def checkout_cart(item, quantity):
    if item in products and products[item]["quantity"] >= quantity:
        cust_cart[item] = cust_cart.get(item, 0) + quantity
        products[item]["quantity"] -= quantity
        print(f"{quantity} {item}(s) added to cart.")
    else:
        print("Unfortunately, there is not enough of this item in stock.")
# This function allows for the users to remove items from their carts, if necessary.
def remove_from_cart(item):
    if item in cust_cart:
        quantity_to_return = cust_cart[item]
        products[item]["quantity"] += quantity_to_return
        del cust_cart[item]
        print(f"{item} removed from cart.")
    else:
        print("Item not in cart.")

def view_cart():
    if not cust_cart:
        print("Your cart is empty.")
    else:
        print("\n************ Best Buy Shopping Cart ************")
        for item, qty in cust_cart.items():
            price = products[item]["price"]
            total = price * qty
            print(f"{item}: {qty} x ${price} = ${total}")
        print("**************************************************")

# Checkout_till function, performs the calculation of all products and quantities and returns the sum, the tax is then added and the discount is calculated if applicable
def checkout_till():
    subtotal = sum(products[item]["price"] * qty for item, qty in cust_cart.items())
    sales_tax = subtotal * 0.10
    discount = 0.05 * subtotal if subtotal > 5000 else 0
    total_due = subtotal + sales_tax - discount

    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Sales Tax (10%): ${sales_tax:.2f}")
    print(f"Discount (5% for bills over $5000): -${discount:.2f}")
    print(f"Total Due: ${total_due:.2f}")

    while True:
        try:
            total_paid = float(input("Enter amount received: ")) # input accepted as floats, just to make it flexible and accept all all possible number combinations, including coins which are represented as decimals
            if total_paid >= total_due:
                change = total_paid - total_due
                print(f"Change due: ${change:.2f}")
                break
            else:
                print("Insufficient amount. Please enter the correct amount.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def cust_receipt():
    if not cust_cart:
        print("Your cart is empty. Add items before checking out.")
        return

    print("\n************Best Buy Retail Store************")
    print("Item\t\tQty\tPrice\tTotal")
    for item, qty in cust_cart.items():
        price = products[item]["price"]
        total = price * qty
        print(f"{item}\t\t{qty}\t${price}\t${total}")
    print("**********************************************")
    checkout_till() # Returns all the products and quantities in the cart, as-well as the various sums and totals, formatted to print like an actual receipt
    print("\nThank you for shopping with us! Come again soon!")

def main():
    while True:
        print("\n1. Add Item to Cart") # When this option is selected, the cashier will be prompted to input the product name and quantity.
        print("2. Remove Item from Cart")
        print("3. View Cart")
        print("4. Checkout") # if the cashier selects option 4, this call all the checkout_till function to complete the payment process and generating the receipt from the cust_receipt function
        print("5. Exit")

        choice = input("Enter your choice: ")
#below are all our conditionals, they just execute the code to represent whatever action is required.
        if choice == "1":
            item = input("Enter product name: ").title()
            if item in products:
                try:
                    qty = int(input("Enter quantity: "))
                    checkout_cart(item, qty)
                except ValueError:
                    print("Invalid quantity! Please enter a number.")
            else:
                print("Item not found. Please enter a valid product name.")

        elif choice == "2":
            item = input("Enter product name: ").title()
            remove_from_cart(item)

        elif choice == "3":
            view_cart()

        elif choice == "4":
            cust_receipt()

        elif choice == "5":
            print("You chose to exit point of sales system.Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")
main()


