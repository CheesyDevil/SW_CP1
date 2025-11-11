#SW 2nd Order Up


entre={ #dictionary of all entres and their prices
    "T-bone":17.99,
    "ice block":12.87,
    "paper salad":3.99,
    "Uranium-235":521.76
}

drink={ #dictionary of all drinks and their prices
    "soda":3.99,
    "murcury":48.99,
    "olive oil": 15.99,
    "gasoline": 99.99
}

side={ #dictionary of all sides and their prices
    "dried paris green":7.99,
    "fries":6.99,
    "unseasoned avocado": 8.99,
    "white Truffles": 990.99
}

total=0



for key in entre.keys():#printing entre costs
    print(f"the {key} costs ${entre[key]}")
ent=input(f"Type '1' for T-bone, '2' for iceblock, '3' for paper salad and '4' for uranium-235\nwhat would you like your entre to be?\n ")#input for choosing entre

if ent=='1':
    total+=entre["T-bone"]