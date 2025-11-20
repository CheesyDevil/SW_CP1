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