"""
what is factorial?
    The factorial of a non-negative integer is the product of all positive
    integers less than or equal to that number

Formula: (n! = n * (n - 1) * (n - 2) * ... * 1)
Special rule: (0! = 1) by mathematical convention.

Examples:
    (3! = 3 * 2 * 1 = 6)
    (4! = 4 * 3 * 2 * 1 = 24)
    (5! = 5 * 4 * 3 * 2 * 1 = 120)
"""


#Using math.factorial()

from math import factorial


while True:
    try:
        n = int(input("Enter a positive number: "))
        result = factorial(n)
        print(result)
        break
    except ValueError:
        print("Please enter a positive integer")

#--------------------------------------------------------------

#Using NumPy's np.prod()
"""
If you don't have numpy on your machine, install it with pip:
    $ pip install numpy
"""

from numpy import prod

n = int(input("Enter a positive number: "))
if n >= 0:
    result = prod(range(1, n + 1))
    print(result)
else:
    print("Please enter a positive integer")


#--------------------------------------------------------------

#Using For Loop

n = int(input("Enter a positive integer: "))
if n > 0:
    f = 1
    for i in range(1, n + 1):
        f *= i
    print(f"Factorial of {n} is {f}")
else:
    print("Please enter a positive integer")


#--------------------------------------------------------------

#Using Recursive Function

def factorial(n):
    if n < 0:
        return "Please enter a positive integer"
    return 1 if n <= 0 else n * factorial(n -1)

num = int(input("Enter a positive integer: "))

print(f"Factorial of {num} is {factorial(num)}")