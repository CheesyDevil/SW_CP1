# SW 2nd Basic claculator

num1=float(input("gimme numbies: "))
num2=float(input("More! "))

print('Addition: ', num1 , "+" , num2 ,"=" , round((num1+num2), 2))
print('Subtraction: ', num1 , "-" , num2 ,"=" , round((num1-num2), 2))
print('Multiplication: ', num1 , "*" , num2 ,"=" , round((num1*num2), 2))
print('Division: ', num1 , "/" , num2 ,"=" , round((num1/num2), 2))
print('Exponent: ', num1 , "^" , num2 ,"=", round((num1**num2) ,2 ))
print('Modulo: ', num1 , "%" , num2 ,"=" , round((num1%num2),2))
print('Integer division: ', num1 , "//" , num2 ,"=" , round((num1//num2), 2))