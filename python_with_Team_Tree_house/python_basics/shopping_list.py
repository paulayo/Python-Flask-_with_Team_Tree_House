# make a list to hold onto shopping items
shopping_list = []

# print instructions on our to use the App
def show_help():
    '''
    The shopping instructions would allow the
    user to choose from a list of instructions.
    '''
    print('What should we pick up at the store? ')
    print('''
    Enter "DONE"  to stop adding items.
    Enter "HELP" for this help.
    Enter "SHOW"  to see your current list.''')


def show_list():
    print("Here's your list")
    for item in shopping_list:
            print(item)


def add_to_list(new_item):
    shopping_list.append(new_item)
    print("Added {}. List now has {} items. ".format(new_item, len(shopping_list)))


print(show_help())

while True:
    ask_shopping_request = input(">  ")
    if ask_shopping_request == 'DONE'.lower():
        break
    elif ask_shopping_request == 'HELP'.lower():
        print(show_help())
        continue
    elif ask_shopping_request  == "SHOW".upper():
        show_list()
        continue
    add_to_list(ask_shopping_request)

show_list()

# add a new item to how list
def addNewItem():
        pass
# be able to quit the App
def quitShopping():
    pass
# print out the list
def getShoppingList():
    pass
