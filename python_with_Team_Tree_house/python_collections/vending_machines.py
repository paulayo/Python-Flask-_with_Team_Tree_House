sodas = ["Pepsi", "Cherry Coke Zero", "Sprite"]
chips = ["Doridos", "Fritos"]
candy = ["Snickers", "M&Ms", "Twizzlers"]


while True:
    choice = input("would you like a SODA, some CHIPS, or a CANDY? ").lower()

    try:

        if choice == 'soda':
            snack = sodas.pop()
        elif choice == "chips":
            snack = chips.pop()
        elif choice == "candy":
            snack = candy.pop()
        else:
            print("I didn't understand that.")
            continue
    except IndexError:
        print("We are all out of {}. Sorry!".format(choice))
    else:
        print("Here's your {}: {}".format(choice,snack))
