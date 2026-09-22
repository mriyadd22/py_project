"""
Let's explore different methods to add two numbers in Python.
"""

#Using + Operator
while True:
    try:
        num1 = float(input("Enter the 1st number: "))
        num2 = float(input("Enter the 2nd number: "))
        result = num1 + num2
        print("The result is: ", result)
        break
    except ValueError:
        print("Please enter a valid number")

#--------------------------------------------------------------

#Using sum() Function
nums = [12, 13]
print(sum(nums))


#--------------------------------------------------------------

#Using operator.add()
from operator import add
print(add(10, 20))

#--------------------------------------------------------------
#Using math.fsum()
"""
The fsum() function from the math module is used for precise floating-point addition. 
It helps reduce rounding errors while adding decimal values.
"""
from math import fsum
nums = [0.12, 1.13]
print(fsum(nums))

