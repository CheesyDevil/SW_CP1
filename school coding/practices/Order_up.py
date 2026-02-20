#SW 2nd Order Up


entre={ #dictionary of all entres and their prices
    "T-bone":17.99,
    "ice block":12.87,
    "paper salad":3.99,
    "Uranium-235":521.76
}

entre_key={ #dictionary of all entres and their numbers
    1:"T-bone",
    2:"ice block",
    3:"paper salad",
    4:"Uranium-235"
}

drink={ #dictionary of all drinks and their prices
    "soda":3.99,
    "murcury":48.99,
    "olive oil": 15.99,
    "gasoline": 99.99
}

drink_key={ #dictionary of all drinks and their numbers
    1:"soda",
    2:"murcury",
    3:"olive oil",
    4:"gasoline"
}

side={ #dictionary of all sides and their prices
    "dried paris green":7.99,
    "fries":6.99,
    "unseasoned avocado": 8.99,
    "white truffles": 1999.99
}

side_key={ #dictionary of all sides and their numbers
    1:"dried paris green",
    2:"fries",
    3:"unseasoned avocado",
    4:"white truffles"
}

total=0

order="" #string for the items that are ordered
def main(menu, menu_key):
    if len(order)==0:
        menu=entre
        menu_key=entre_key
    elif len(order)==1:
        menu=drink
        menu_key=drink_key
    elif len(order)==2 or len(order)==3:
        menu=side
        menu_key=side_key

    for key in menu.keys():#printing entre costs
        print(f"the {key} costs ${menu[key]}")
    ent=input(f"Type '1' for {menu_key[1]}, '2' for {menu_key[2]}, '3' for {menu_key[3]} and '4' for {menu_key[4]}\nwhat is your choice?\n ")#input for choosing dish


    if ent=='1'or ent=='2'or ent=='3'or ent=='4': #checking if input is valid
        ent_nam=menu_key[int(ent)]
        total+=menu[ent_nam]
        order=order+(f"For your entre you ordered the {ent_nam}\n")
    else:
        print("please enter a valid order")

while len(order)==1: #loop for drink ordering
    for key in drink.keys():#printing drink costs
        print(f"the {key} costs ${drink[key]}")
    drk=input(f"Type '1' for soda,\n'2' for murcury,\n'3' for olive oil\nand '4' for gasoline\nwhat would you like your drink to be?\n ")#input for choosing drink

    if drk=='1'or drk=='2'or drk=='3'or drk=='4': #checking if input is valid
        drk_nam=drink_key[int(drk)]
        total+=drink[drk_nam]
        order=order+(f"For your drink you ordered a glass of {drk_nam}\n")
    else:
        print("please enter a valid order")

while len(order)==2 or len(order)==3: #loop for side ordering, makes it run twice
    for key in side.keys():#printing side costs
        print(f"the {key} costs ${side[key]}")
    sid=input(f"Type '1' for dried paris green,\n'2' for fries,\n'3' for unseasoned avocado\nand '4' for white truffles\nwhat would you like your side to be?\n ")#input for choosing sides

    if sid=='1'or sid=='2'or sid=='3'or sid=='4': #checking if input is valid
        sid_nam=side_key[int(sid)]
        total+=side[sid_nam]
        order=order+(f"You ordered a small plate of {sid_nam} \n")
    else:
        print("please enter a valid order")

order=order+(f"The final cost comes out to ${total}")

print(order)


#CHANGE TO INCORPERATE FUNCTIONS