shopping_cart = [] # list of dictionaries to store items
def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    qty = int(input("Enter quantity: "))
    item = {"name": name, "price": price, "quantity": qty}
    shopping_cart.append(item)
    print(f"✅ {qty} x {name} added to your cart!")
def view_cart():
    if not shopping_cart:
        print("\n🛍️ Your shopping cart is empty.")
        return
    else:
        print("\n🛒 Your shopping cart:")
        total_items = 0
        total_price = 0
    for item in shopping_cart:
        item_total = item["price"] * item["quantity"]
        total_items += item["quantity"]
        total_price += item_total
        print(f"- {item['name']} (x{item['quantity']}): ₹{item_total:.2f}")
        print(f"\nTotal items: {total_items}")
        print(f"Total price: ₹{total_price:.2f}")
def main():
    print("Welcome to your shopping cart! 🛍️")
    while True:
        print("\nPlease choose an option:")
        print("1. Add item")
        print("2. View cart")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_item()
        elif choice == "2":
            view_cart()
        elif choice == "3":
            print("🛒 Thank you for shopping! Goodbye.")
            break
        else:
            print("❌ Invalid choice. Try again.")
if __name__ == "__main__":
    main()