shopping_cart = []
running = True
if __name__ == "__main__":
    print('Welcome to your shopping cart.')

def add_item():
    add=input('Add item: ')
    shopping_cart.append(add)
    return shopping_cart
def view_cart():
    if not shopping_cart:
        print('No items in cart!')
    else:
        print(shopping_cart)

while running:
    print('\n')
    print('Please choose your option')
    print('1.Add items')
    print('2.view cart')
    print('3.Done')


    choice= int(input('Enter your choice: '))
    if choice == 1:
        add_item()
    elif choice == 2:
        view_cart()
    else:
        break
continue_shopping = input('Do you want to refresh your cart? yes/no')

