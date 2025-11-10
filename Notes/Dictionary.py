#SW 2nd Dictionary Notes


#What are dictionaries?
    #A data type that containes a set of key and value pairs that can be easily accessed
#How do dictionaries simplify variables in a project?
    #they can be used to access many variables more simply
#What are key and value pairs?
    # a pair that contains the key that is either a number or a string that is used to access the value which can be any variable
#How do you build a dictionary?
names={
    "key":"value",
    "Lucy":20,
    "Hannah":19
}
#How do you call a value from a dictionary?
print(names["Lucy"])
#How do you get each of the keys from a dictionary?
print(names.keys)
#How do you update a value in a dictionary?
names["age"]+=1
#Can you add new key and value pairs to a dictionary during runtime?
names['Seth']=15 #yes

names={
    "key":"value",
    "Lucy":20,
    "Hannah":19,

}
print(names["Lucy"])
print(names.keys)
for key in names.keys():
    print(f"{key} is {names[key]}")