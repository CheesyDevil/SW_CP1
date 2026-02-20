#SW 2nd Formating Outputs notes

#How do I write the format method?
name="seth"
age=42
print("Hello {}, nice to meet you. You are {:E}, that is really old.".format(name,age))

#What does the format method allow me to change about my outputs?
  # colon something {:...}
#Describe why it is important to format your outputs
  #So you can tell what is going on.
#What is an f-string?
  # A better version of the basic formatting
#How do I create and f-string?
print(f"Hello {name}, nice to meet you. You are {age:E}, that is really old.")
#What do f-strings allow me to do?
  #make my code very readable

#{:,} makes gives commas to number.
#{:b} makes number bianary
#{:E} makes number scientific notation
#{:%} Makes number a percent
#{:.2f} Makes it a decimal to the second
#\n swithes line