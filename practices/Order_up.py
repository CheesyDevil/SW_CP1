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
    "white truffles": 990.99
}

side_key={ #dictionary of all sides and their numbers
    1:"dried paris green",
    2:"fries",
    3:"unseasoned avocado",
    4:"white truffles"
}

total=0

order=[]#list for the items that are ordered


for key in entre.keys():#printing entre costs
    print(f"the {key} costs ${entre[key]}")
ent=input(f"Type '1' for T-bone, '2' for iceblock, '3' for paper salad and '4' for uranium-235\nwhat would you like your entre to be?\n ")#input for choosing entre

while len(order)==0: #loop for entre ordering
    for key in entre.keys():#printing entre costs
        print(f"the {key} costs ${entre[key]}")
    ent=input(f"Type '1' for T-bone,\n'2' for iceblock,\n'3' for paper salad and\n'4' for uranium-235\nwhat would you like your entre to be?\n ")#input for choosing entre

    if ent=='1':
        total+=entre[entre_key[1]]
        order.append(entre_key[1])
    elif ent=='2':
        total+=entre[entre_key[2]]
        order.append(entre_key[2])
    elif ent=='3':
        total+=entre[entre_key[3]]
        order.append(entre_key[3])
    elif ent=='4':
        total+=entre[entre_key[4]]
        order.append(entre_key[4])
    else:
        print("please enter a valid order")

while len(order)==1: #loop for drink ordering
    for key in drink.keys():#printing drink costs
        print(f"the {key} costs ${drink[key]}")
    drk=input(f"Type '1' for soda,\n'2' for murcury,\n'3' for olive oil\nand '4' for gasoline\nwhat would you like your drink to be?\n ")#input for choosing drink

    if drk=='1':
        total+=drink[drink_key[1]]
        order.append(drink_key[1])
    elif drk=='2':
        total+=drink[drink_key[2]]
        order.append(drink_key[2])
    elif drk=='3':
        total+=drink[drink_key[3]]
        order.append(drink_key[3])
    elif drk=='4':
        total+=drink[drink_key[4]]
        order.append(drink_key[4])
    else:
        print("please enter a valid order")

while len(order)==2 or len(order)==3: #loop for side ordering, makes it run twice
    for key in side.keys():#printing side costs
        print(f"the {key} costs ${side[key]}")
    sid=input(f"Type '1' for dried paris green,\n'2' for fries,\n'3' for unseasoned avocado\nand '4' for white truffles\nwhat would you like your side to be?\n ")#input for choosing sides

    if sid=='1'or sid=='2'or sid=='3'or sid=='4':
        sd=drink_key[int(sid)]
    else:
        print("please enter a valid order")

print(f"Your final order is {}")