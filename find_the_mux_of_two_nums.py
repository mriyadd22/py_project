"""
Find the Maximum of two numbers in Python
"""
#Using max() function ---> (max() function compares two or more values and returns the largest one)

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
print(max(num1, num2))

#--------------------------------------------------------------
#Using ternary operator
"""
Ternary conditional operator evaluates a condition and returns one of two values 
depending on whether the condition is true or false in a single expression.
"""

num1 = 20
num2 = 15
print(num1 if num1 > num2 else num2)

#--------------------------------------------------------------
#Using if-Else statement
a = 7
b = 9

if a > b:
    print(a)
else:
    print(b)
