menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cake', 
        "price": 2.79},
    4: {"name": 'soup', 
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}

def calculate_subtotal(order):
    print('Calculating bill subtotal...')
    items = []
    items  = [item["name"] for item in order]
    items_price = []
    items_price = [item["price"] for item in order]
    subtotal = round(items_price[0] + items_price[1] + items_price[2],2)
    items_dict = (items,subtotal)
    print(items_dict)
    return(subtotal)
    

    

def calculate_tax(subtotal):
    print('Calculating tax from subtotal...')
    # items_price = []
    # items_price = [item["price"] for item in order]
    # subtotal = round(items_price[0] + items_price[1] + items_price[2],2)
    tax = (subtotal  * 0.15  )
    tax = round(tax ,2)
    print("Tax for the order is: " + str(tax))
    return(tax)
   

def summarize_order(order):
    print("summarizing your order....")
    items_price = []
    items_price = [item["price"] for item in order]
    subtotal = round(items_price[0] + items_price[1] + items_price[2],2)
    names = []
    names = [item["name"] for item in order]
    tax = subtotal * 15 / 100
    total = round(subtotal + tax, 2)
    sum_order = (names,(round(total,2)))
    print(sum_order)
    return(names,total)


   

# This function is provided for you, and will print out the items in an order


def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order
# This function is provided for you, and will display the menu
def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()

# This function is provided for you, and will create an order by prompting the user to select menu items
def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order


def main():
    order = take_order()
    print_order(order)
    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is: " + str((subtotal)))
    calculate_tax(subtotal) 
    summarize_order(order)

    

   

if __name__ == "__main__":
    main()
