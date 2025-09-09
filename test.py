original_string = "Python"
char_to_insert = "-"
# Convert string to a list of characters, insert the new character, then join
char_list = list(original_string)
char_list.insert(3, char_to_insert) # Insert at index 3
new_string = "".join(char_list)
print(new_string)
#practice sync