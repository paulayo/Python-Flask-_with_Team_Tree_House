import os

# make a list to hold onto shopping items
shopping_list = []

# declare a clear screen function

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# print instructions on our to use the App
def show_help():
    '''
    The shopping instructions would allow the
    user to choose from a list of instructions.
    '''
    clear_screen()
    print('What should we pick up at the store? ')
    print('''
    Enter "DONE"  to stop adding items.
    Enter "HELP" for this help.
    Enter "SHOW"  to see your current list.
    Enter "REMOVE" to delete an item from your List''')


def show_list():

    clear_screen()

    print("Here's your list")

    for index, item in enumerate(shopping_list, start=1):
        print(f"{index}. {item}.")

    print("-"*10)


def add_to_list(item):
    '''
    The function would allow the user
    to make input of goods(as a reminder) to add to
    to list for purchase.
    The items in would be shown to
    user as new items are added to list.
    Also, when users input negative values
    the app will show none.
    '''
    show_list()

    if len(shopping_list):
        position = input("Where should I add {}?\n"
                        "Press Enter to add to the end of the list\n"
                        ">  ".format(item))
    else:
        position = 0

    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position-1, item)
    else:
        shopping_list.append(new_item)

    show_list()


def remove_from_list():

    show_list()

    what_to_remove = input("What would you like to remove?\n>  ")

    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        pass
    show_list()



print(show_help())

while True:
    new_item = input(">  ")
    if new_item.upper() == "DONE" or new_item.upper() == "QUIT":
        break
    elif new_item.upper() == "HELP":
        print(show_help())
        continue
    elif new_item.upper()  == "SHOW":
        show_list()
        continue
    elif new_item.upper() == "REMOVE":
        remove_from_list()
    else:
        add_to_list(new_item)

show_list()
