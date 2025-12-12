def print_list_contents(*args):
    """
    Prints each item passed as an argument.
    """
    print("Printing list contents:")
    for item in args:
        print(item)

# Example usage:
my_list = [1, 2, 3, "hello", True]
print_list_contents(*my_list)


#git config --global user.name "github username"
#git config --global user.email "github email"
print('██')
print(f"\033[96m{my_list[1]}\033[0m")


x=1
y=3
print(x)
print(y)
def add(x,y):
    x+=1
    y+=1
    return x , y
x=(add(x,y)[0])
y=add(x,y)[1]
print(x)
print(y)