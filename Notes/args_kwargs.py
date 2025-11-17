#SW 2nd *ARGS and **KWARGS notes


#What are positional arguments?
    #Arguements that change based on where thay are put in a function
#What are keyword arguments?
    #Arguements that use key words to detemine what goes where
"""def hello(name, age):
    return f'Hello {name}! you are {age}'

print(hello(name="treyson",age=19))"""
#How do you set a default parameter value?
    # by setting the positional arguement as a value
"""def hello(name="John", age=42):
    return f'Hello {name}! you are {age}'

print(hello("treyson",19))"""
#How do you alter a function to take in an unknown number of arguments?
    #by using *args and **kwargs



#positional arguements, *args, Keyword arguements, **kwargs
def hello(*names, **last):
    print(type(names))
    for name in names:
        print(f'Hello {name}, {last}')

hello('johnson',"treyson","John","jacob")
