def print_list_contents(*args):
    """
    Prints each item passed as an argument.
    """
    print("Printing list contents:")
    for item in args:
        print(item)

# Example usage:
"""my_list = [1, 2, 3, "hello", True]
print_list_contents(*my_list)"""


#git config --global user.name "github username"
#git config --global user.email "github email"
print('██')
print(f"\033[96m██\033[0m")

"""z=3
x=int(input())
y=3
print(x)
print(y)
def add(x,y,):
    x+=1
    y+=1
    print("print")
    return x , y
if add(x,y)[0]:
    x=add(x,y)[0]
    y=add(x,y)[1]
    print(x)
    print(y)
else:
    print("x=0")"""
"""x=1.9
print(x)
x=int(x)
print(x)"""
import sys
import time

def slow_print(text, delay=0.05):
    """
    Prints text one character at a time with a delay to simulate typing.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush() # Forces the character to be printed immediately
        time.sleep(delay)  # Pauses for a short duration

    print()# Prints a final newline character after the text is done

# --- Usage Examples ---
slow_print("Welcome to the program! This text is typing out slowly.")
slow_print("Here is another line with a custom, faster delay.", delay=0.02)