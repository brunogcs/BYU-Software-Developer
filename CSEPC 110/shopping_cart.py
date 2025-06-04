"""
Creativity Part

1 - Prevention of Duplicate Items: the program checks if new_item is already in the cart.
2 - Empty Cart Message in Options 2 and 3: the program checks if the cart is empty (len(cart) == 0) and warns the user.
3 - Index Validation When Removing: the code catches an error if the user inputs something that isn't a number.
"""

print("Welcome to the Shopping Cart Program!")
user_option = 0
cart = []
price = []

while user_option!= 5:
    
    options = ("""
    1 - Add a new item
    2 - Display the contents of the shopping cart
    3 - Remove an item
    4 - Compute the total 
    5 - Quit
    """)
    try:
        user_option = int(input(f"""
        Select one of these options bellow:
        {options}
        input: 
        """
        ))
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 5.")
        continue
    if user_option < 1 or user_option > 5:
        print("Invalid option. Please choose a number between 1 and 5.")
        continue

    if user_option == 1:
        while True:
            new_item = input("What item do you want to add? ")
            if new_item in cart:
                print("The item already exists. Please enter a different item.")
            else:
                cart.append(new_item)
                new_price = float(input(f"What is the price of '{new_item}'? "))
                price.append(new_price)
                print(f"'{new_item}' has been added to the cart at ${new_price:.2f}.")
                break

    if user_option == 2:
        if len(cart) == 0:
            print("The shopping cart is empty.")
        else:
            print("The contents of the shopping cart are:")
            for i, (item, value) in enumerate(zip(cart, price), start=1):
                print(f"{i}. {item} - ${value:.2f}")

    if user_option == 3:
        if len(cart) == 0:
            print("The shopping cart is empty. Nothing to remove.")
            continue  # volta ao menu
        print("The contents of the shopping cart are:")
        for i, (item, value) in enumerate(zip(cart, price), start=1):
            print(f"{i}. {item} - ${value:.2f}")

        while True:
            try:
                delete_item = int(input("Which item would you like to remove? "))
            except ValueError:
                print("Invalid input. Please enter the item numbe")
                continue

            index_delete = delete_item - 1
            if index_delete < 0 or index_delete >= len(cart):
                print("Sorry, that is not a valid item number. Please try again.")
            else:
                removed_name = cart.pop(index_delete)
                price.pop(index_delete)
                print(f"Item '{removed_name}' removed.")
                break

    if user_option == 4:
        total_price = 0
        for value in price:
            total_price += value
        print(f"The total price of the items in the shopping cart is ${total_price:.2f}")

    if user_option == 5:
        print("Thank you. Goodbye.")
        break
