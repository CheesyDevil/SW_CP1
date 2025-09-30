# SW 2nd Shopping List Manager

list=[]

while True:
    action = input("\nuse 'add' to add and item to the list\nuse 'remove' to remove an item from the list\nuse'view'to view your current list\nuse 'exit' to finalize list\n\nplease add an input here: ")
    if action=="add":
        item=input("\nwhat would you like to add to the list: \n")
        list.append(item)
        print(f"\n{item} added\n")
    elif action=="remove":
        item=input("\nWhich item would you like to remove: \n")
        if item in list:
            position=list.index(item)
            list.pop(position)
            print(f"\n{item} removed\n")
        else:
            print("\nplease enter a valid item.\n")
    elif action=="view":
        print("\n", list, "\n")
    elif action == "exit":
        break
    else:
        print("\nplease enter a valid action.\n")
print(f"\nyour final list is {list}.\n")